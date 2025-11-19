from flask import Flask, request, render_template, redirect, url_for
import mysql.connector, os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__, template_folder='WebHTML')

def getConnection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database="CrimeData"
    )


@app.route('/')
def index():
    conn = getConnection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM PrimaryOfficer")
    officers = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('input.html', officers=officers)

@app.route('/create', methods=['POST'])
def create_officer():
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    badgeNumber = request.form['badgeNumber']
    officerRank = request.form['officerRank']
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("INSERT IGNORE INTO Person (firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
    cursor.execute(
        "INSERT INTO PrimaryOfficer (firstName, lastName, badgeNumber, officerRank) VALUES (%s, %s, %s, %s)",
        (firstName, lastName, badgeNumber, officerRank)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))


@app.route('/update/<firstName>/<lastName>', methods=['GET', 'POST'])
def update_officer(firstName, lastName):
    conn = getConnection()
    cursor = conn.cursor(dictionary=True)
    if request.method == 'POST':
        fn = request.form['firstName']
        ln = request.form['lastName']
        badgeNumber = request.form['badgeNumber']
        officerRank = request.form['officerRank']
        cursor.execute(
            "UPDATE PrimaryOfficer SET firstName=%s, lastName=%s, badgeNumber=%s, officerRank=%s WHERE firstName=%s AND lastName=%s",
            (fn, ln, badgeNumber, officerRank, firstName, lastName)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    cursor.execute("SELECT * FROM PrimaryOfficer WHERE firstName=%s AND lastName=%s", (firstName, lastName))
    officer = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('update.html', officer=officer)

@app.route('/delete/<firstName>/<lastName>')
def delete_officer(firstName, lastName):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM PrimaryOfficer WHERE firstName=%s AND lastName=%s", (firstName, lastName))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))


@app.route('/showSuspects', methods=['GET'])
def showSuspects():
    conn = getConnection()
    cursor = conn.cursor(dictionary=True)
    caseNumber = request.args.get('caseNumber')
    if caseNumber is not None:
        cursor.execute("""SELECT s.firstName, s.lastName, s.age
                          FROM CaseSuspect cs
                          JOIN Suspect s ON cs.firstName = s.firstName AND cs.lastName = s.lastName
                          WHERE cs.caseNumber=%s""", (caseNumber,))
        suspects = cursor.fetchall()
        pageTitle = f"Suspects for Case {caseNumber}"
    else:
        cursor.execute("SELECT firstName, lastName, age FROM Suspect")
        suspects = cursor.fetchall()
        pageTitle = "All Suspects"
    cursor.close()
    conn.close()
    return render_template('suspects.html', suspects=suspects, pageTitle=pageTitle)

@app.route('/createSuspect', methods=['POST'])
def create_suspect():
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    age = request.form['age']
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("INSERT IGNORE INTO Person (firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
    cursor.execute("INSERT INTO Suspect (firstName, lastName, age) VALUES (%s, %s, %s)", (firstName, lastName, age))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('showSuspects'))

@app.route('/assignSuspect', methods=['POST'])
def assignSuspect():
    caseNumber = request.form['caseNumber']
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO CaseSuspect (caseNumber, firstName, lastName) VALUES (%s, %s, %s)",
        (caseNumber, firstName, lastName))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('showCasefiles', firstName=firstName, lastName=lastName))


@app.route('/showCasefiles', methods=['GET'])
def showCasefiles():
    conn = getConnection()
    cursor = conn.cursor(dictionary=True)
    firstName = request.args.get('firstName')
    lastName = request.args.get('lastName')
    if firstName and lastName:
        cursor.execute("""SELECT c.caseNumber, c.status, c.officerFirstName, c.officerLastName
                          FROM CaseFile c
                          JOIN CaseSuspect cs ON c.caseNumber = cs.caseNumber
                          WHERE cs.firstName=%s AND cs.lastName=%s""", (firstName, lastName))
        casefiles = cursor.fetchall()
        pageTitle = f"Casefiles for Suspect: {firstName} {lastName}"
    else:
        cursor.execute("SELECT * FROM CaseFile")
        casefiles = cursor.fetchall()
        pageTitle = "All Casefiles"
    cursor.close()
    conn.close()
    return render_template('casefiles.html',
                           casefiles=casefiles,
                           pageTitle=pageTitle,
                           firstName=firstName,
                           lastName=lastName)

@app.route('/createCasefile', methods=['POST'])
def create_casefile():
    caseNumber = request.form['caseNumber']
    status = request.form['status']
    officerFirstName = request.form['officerFirstName']
    officerLastName = request.form['officerLastName']
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO CaseFile (caseNumber, status, officerFirstName, officerLastName) VALUES (%s, %s, %s, %s)",
        (caseNumber, status, officerFirstName, officerLastName))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('showCasefiles'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009, debug=True)
