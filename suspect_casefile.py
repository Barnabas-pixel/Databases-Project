import mysql.connector, os
from dotenv import load_dotenv
load_dotenv()
import json

load_dotenv()

def getConnection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database="CrimeData"
    )


def printSuspect():
    connection = getConnection()
    mycursor = connection.cursor()
    mycursor.execute("select * from CaseSuspect")
    myresult = mycursor.fetchone()
    
    print("In the suspect table, we have the following items: ")
    while myresult is not None:
        print(myresult)
        myresult = mycursor.fetchone()
    connection.close()
    print()

def printCaseFile():
    connection = getConnection()
    mycursor = connection.cursor()
    mycursor.execute("select * from CaseFile")
    myresult = mycursor.fetchone()

    print("In the casefiles table, we have the following items: ")
    while myresult is not None:
        print(myresult)
        myresult = mycursor.fetchone()
    connection.close()
    print()

 
def printCaseSuspect():
    firstname = input("Enter the suspect's first name: ")
    lastname = input("Enter the suspect's last name: ")

    connection = getConnection()
    mycursor = connection.cursor()

    query = """
        SELECT c.caseNumber, c.status, c.officerFirstName, c.officerLastName
        FROM CaseFile c
        JOIN CaseSuspect cs ON c.caseNumber = cs.caseNumber
        WHERE cs.firstName = %s AND cs.lastName = %s
    """
    mycursor.execute(query, (firstname, lastname))
    myresult = mycursor.fetchone()

    print(f"All case files for suspect {firstname} {lastname}:")
    while myresult is not None:
        print(myresult)
        myresult = mycursor.fetchone()
    connection.close()
    print()


def printSuspectFile():
    case_number = input("Enter the case number: ")

    connection = getConnection()
    mycursor = connection.cursor()

    query = """
        SELECT s.firstName, s.lastName, s.age
        FROM Suspect s
        JOIN CaseSuspect cs ON s.firstName = cs.firstName AND s.lastName = cs.lastName
        WHERE cs.caseNumber = %s
    """
    mycursor.execute(query, (case_number,))
    myresult = mycursor.fetchone()

    print(f"All suspects in case {case_number}:")
    while myresult is not None:
        print(myresult)
        myresult = mycursor.fetchone()
    connection.close()
    print()


def addSuspectToCase():
    caseNumber = input("Enter the case number: ")
    firstName = input("Enter the suspect's first name: ")
    lastName = input("Enter the suspect's last name: ")

    connection = getConnection()
    mycursor = connection.cursor()
    query = "INSERT INTO CaseSuspect (caseNumber, firstName, lastName) VALUES (%s, %s, %s);"
    mycursor.execute(query, (caseNumber, firstName, lastName))
    connection.commit()
    connection.close()


def removeSuspectFromCase():
    caseNumber = input("Enter the case number: ")
    firstName = input("Enter the suspect's first name: ")
    lastName = input("Enter the suspect's last name: ")

    connection = getConnection()
    mycursor = connection.cursor()
    query = "DELETE FROM CaseSuspect WHERE caseNumber=%s AND firstName=%s AND lastName=%s;"
    mycursor.execute(query, (caseNumber, firstName, lastName))
    connection.commit()
    connection.close()

menuText = """Please select one of the following options:
1) Display all suspects
2) Display all case files
3) Display all case-suspect relationships
4) Display all case files for a suspect
5) Add a suspect to a case file
6) Remove a suspect from a case file
q) Quit
"""

if __name__ == "__main__":
    menuOption = ""
    while menuOption != 'q':
        menuOption = input(menuText)
        if menuOption == "1":
            printSuspect()
        elif menuOption == "2":
            printCaseFile()
        elif menuOption == "3":
            printCaseSuspect()
        elif menuOption == "4":
            printSuspectFile()
        elif menuOption == "5":
            addSuspectToCase()
        elif menuOption == "6":
            removeSuspectFromCase()
