from sqlalchemy.orm import sessionmaker
from models import Property
from db import engine

Session = sessionmaker(bind=engine)

def add_property():
    session = Session()
    address = input("Enter property address: ")
    rent = input("Enter property rent: ")

    property = Property(address=address, rent=rent)
    session.add(property)
    session.commit()
    print("Property added successfully.")

def display_properties():
    session = Session()
    properties = session.query(Property).all()
    if properties:
        print("===== Properties List =====")
        for prop in properties:
            print(f"ID: {prop.id}, Address: {prop.address}, Rent: {prop.rent}")
    else:
        print("No properties found.")
    session.close()

def property_management_menu():
    while True:
        print("===== Property Management Menu =====")
        print("1. Add Property")
        print("2. Display Properties")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_property()
        elif choice == '2':
            display_properties()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a valid option.")