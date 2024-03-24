from sqlalchemy.orm import sessionmaker
from models import UnderConstructionProperty
from db import engine

Session = sessionmaker(bind=engine)

def add_under_construction_property():
    session = Session()
    name = input("Enter property name under construction: ")

    property = UnderConstructionProperty(name=name)
    session.add(property)
    session.commit()
    print("Under construction property added successfully.")
    session.close()

def display_under_construction_properties():
    session = Session()
    properties = session.query(UnderConstructionProperty).all()
    if properties:
        print("===== Under Construction Properties List =====")
        for prop in properties:
            print(f"ID: {prop.id}, Name: {prop.name}")
    else:
        print("No under construction properties found.")
    session.close()

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