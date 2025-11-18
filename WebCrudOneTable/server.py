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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)

