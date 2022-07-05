import sys
from sqlalchemy import create_engine, Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import Session
from flask_sqlalchemy import SQLAlchemy


# constants
base = declarative_base()
conn_info = {
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": 5432,
    "dbname": "test"
}


class People(base):  
    __tablename__ = 'people'

    id = Column(Integer, primary_key = True)
    first_name = Column(String)
    last_name = Column(String)
    dob = Column(Date)


def get_url(user:str, password:str, host:str, port:int, dbname:str) -> str:
    url = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"

    return url


def instructions() -> None:
    print("\n\nKEYS ->\n")
    print("CREATE : create and add data to the database.")
    print("READ : view the database.")
    print("UPDATE : update/ change existing data in the database.")
    print("DELETE : delete data in the database.")
    print("QUIT : close program.")
    print("INSTRUCTIONS : view these instructions again.\n")


def get_user_key() -> str:
    key = input("\nEnter key: ")
    print()
    key = key.upper()

    return key


def execute_operations(key:str, session) -> None:
    if key == "CREATE":
        create(session)
    elif key == "READ":
        read(session)
    elif key == "UPDATE":
        update(session)
    elif key == "DELETE":
        delete(session)
    elif key == "INSTRUCTIONS":
        instructions()
    elif key == "QUIT":
        sys.exit()
    else:
        print("Not a key.\n")


def create(session:None) -> None:
    new_first_name = input("\nEnter first name: ")
    new_first_name = new_first_name.capitalize()
    new_last_name = input("Enter last name: ")
    new_last_name = new_last_name.capitalize()
    new_dob = input("Enter date of birth (yyyy-mm-dd): ")

    people = session.query(People)

    for person in people:
        if new_first_name == person.first_name and new_last_name == person.last_name:
            print("Person already in database.")
            return
        else:
            new_person = People(first_name = new_first_name, last_name = new_last_name, dob = new_dob)
            session.add(new_person)
            session.commit()
            return 

    new_person = People(first_name = new_first_name, last_name = new_last_name, dob = new_dob)
    session.add(new_person)
    session.commit()
    return 


def read(session:None) -> None:
    people = session.query(People)
    for person in people:
        print(person.first_name, person.last_name, person.dob)


def update(session:None) -> None:
    print("\nTo update a persons data, start by entering the first and last name of the person you wish to update.")
    print()

    prev_first_name = input("Enter previous first name: ")
    prev_first_name = prev_first_name.capitalize()
    prev_last_name = input("Enter previous last name: ")
    prev_last_name = prev_last_name.capitalize()
    
    print("\nNow update the person with their new data.\n")
    print()

    updated_first_name = input("Enter updated first name: ")
    updated_first_name = updated_first_name.capitalize()
    updated_last_name = input("Enter updated last name: ")
    updated_last_name = updated_last_name.capitalize()
    updated_dob = input("Enter updated date of birth (yyyy-mm-dd): ")

    people = session.query(People)
    updated = False
    for person in people:
        if person.first_name == prev_first_name:
            if person.last_name == prev_last_name:
                person.first_name = updated_first_name
                person.last_name = updated_last_name
                person.dob = updated_dob
                updated = True
                session.commit()

    if updated:
        print("Successfully updated")
        print()
    else:
        print("Could not update.")
        print()


def delete(session:None) -> None:
    print("\nTo delete a persons data, enter their first and last names.")
    print()

    delete_first_name = input("Enter first name: ")
    delete_first_name = delete_first_name.capitalize()
    delete_last_name = input("Enter last name: ")
    delete_last_name = delete_last_name.capitalize()
    print()

    print("Are you sure you want to delete this data?")
    confirm = input("Enter y/n: ")
    confirm = confirm.lower()

    if confirm == "y":
        people = session.query(People)
        for person in people:
            if person.first_name == delete_first_name:
                if person.last_name == delete_last_name:
                    session.delete(person)
                    session.commit()
                    return


def main() -> None:
    url = get_url(**conn_info)
    engine = create_engine(url)
    session = Session(engine)
    base.metadata.create_all(engine)

    instructions()
    while True:
        key = get_user_key()
        execute_operations(key, session)


if __name__ == "__main__":
    main()