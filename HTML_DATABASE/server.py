from flask import Flask, request, render_template
import mysql.connector, os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__, template_folder='WebPage')
def getConnection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database="CrimeData"
    )

@app.route('/', methods=['GET'])
def index():
    firstName = request.args.get('firstName')
    lastName = request.args.get('lastName')
    badgeNumber = request.args.get('badgeNumber')
    officerRank = request.args.get('officerRank')

    conn = getConnection()
    cursor = conn.cursor(dictionary=True)

    
    if firstName and lastName and badgeNumber and officerRank:
        cursor.execute(
            "INSERT INTO PrimaryOfficer (firstName, lastName, badgeNumber, officerRank) VALUES (%s, %s, %s, %s)",
            (firstName, lastName, badgeNumber, officerRank)
        )
        conn.commit()
    cursor.execute("SELECT * FROM PrimaryOfficer")
    officers = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('input.html', officers=officers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)

