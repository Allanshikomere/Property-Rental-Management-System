from sqlalchemy.orm import sessionmaker
from models import UnderConstructionProperty
from db import engine
import sqlite3

Session = sessionmaker(bind=engine)


conn = sqlite3.connect('property_rental_management.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS under_construction_properties (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
''')
conn.commit()

def add_under_construction_property():
    session = Session()
    name = input("Enter property name under construction: ")

   
    property = UnderConstructionProperty(name=name)
    session.add(property)
    session.commit()
    print("Under construction property added successfully.")

def display_under_construction_properties():
    session = Session()
    properties = session.query(UnderConstructionProperty).all()
    if properties:
        print("===== Under Construction Properties List =====")
        for prop in properties:
            print(f"ID: {prop.id}, Name: {prop.name}")
    else:
        print("No under construction properties found.")

def under_construction_property_management_menu():
    while True:
        print("===== Under Construction Property Management Menu =====")
        print("1. Add Under Construction Property")
        print("2. Display Under Construction Properties")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_under_construction_property()
        elif choice == '2':
            display_under_construction_properties()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

conn.close()
