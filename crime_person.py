import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def connect_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database="CrimeData"
    )

def display_persons(cursor):
    cursor.execute("SELECT * FROM Person;")
    rows = cursor.fetchall()
    print("Person Table:")
    for row in rows:
        print(row)

def insert_person(cursor, db):
    fname = input("First name: ")
    lname = input("Last name: ")
    query = "INSERT INTO Person (firstName, lastName) VALUES (%s, %s)"
    cursor.execute(query, (fname, lname))
    db.commit()
    print("Added.")

def update_person(cursor, db):
    fname = input("First name to update: ")
    new_lname = input("New last name: ")
    query = "UPDATE Person SET lastName = %s WHERE firstName = %s"
    cursor.execute(query, (new_lname, fname))
    db.commit()
    print("Updated.")

def delete_person(cursor, db):
    fname = input("First name to delete: ")
    query = "DELETE FROM Person WHERE firstName = %s"
    cursor.execute(query, (fname,))
    db.commit()
    print("Deleted.")

def main():
    db = connect_db()
    cursor = db.cursor()

    while True:
        print("Menu:")
        print("1) Display Person table")
        print("2) Insert person")
        print("3) Update person")
        print("4) Delete person")
        print("q) Quit")
        choice = input("Choice: ")

        if choice == '1':
            display_persons(cursor)
        elif choice == '2':
            insert_person(cursor, db)
        elif choice == '3':
            update_person(cursor, db)
        elif choice == '4':
            delete_person(cursor, db)
        elif choice.lower() == 'q':
            break
        else:
            print("Invalid choice.")

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
