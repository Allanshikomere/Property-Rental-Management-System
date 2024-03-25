import sqlite3
from sqlalchemy.orm import sessionmaker
from models import Property, Tenant
from db import engine


conn = sqlite3.connect('property_rental_management.db')
cursor = conn.cursor()

# Table for properties
cursor.execute('''
    CREATE TABLE IF NOT EXISTS properties (
        id INTEGER PRIMARY KEY,
        address TEXT,
        rent INTEGER,
        tenant_id INTEGER
    )
''')

# Table for tenants
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tenants (
        id INTEGER PRIMARY KEY,
        name TEXT,
        property_id INTEGER,
        FOREIGN KEY(property_id) REFERENCES properties(id)
    )
''')

conn.commit()
conn.close()

Session = sessionmaker(bind=engine)

def add_property():
    session = Session()
    address = input("Enter property address: ")
    rent = int(input("Enter property rent: "))  

    property = Property(address=address, rent=rent)
    session.add(property)
    session.commit()
    print("Property added successfully.")

def add_tenant():
    session = Session()
    name = input("Enter tenant name: ")

    while True:
        property_address = input("Enter property address: ")
        property = session.query(Property).filter_by(address=property_address).first()
        if property:
            
            tenant = Tenant(name=name, property_id=property.id)
            session.add(tenant)
            session.commit()  
            print("Tenant added successfully.")
            break
        else:
            print("Error: Property address does not exist. Please enter a valid property address.")

    session.close()


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

def display_tenants():
    session = Session()
    tenants = session.query(Tenant).all()
    if tenants:
        print("===== Tenants List =====")
        for tenant in tenants:
            print(f"ID: {tenant.id}, Name: {tenant.name}, Property ID: {tenant.property_id}")
    else:
        print("No tenants found.")
    session.close()

def property_management_menu():
    while True:
        print("===== Property Management Menu =====")
        print("1. Add Property")
        print("2. Display Properties")
        print("3. Add Tenant")
        print("4. Display Tenants")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_property()
        elif choice == '2':
            display_properties()
        elif choice == '3':
            add_tenant()
        elif choice == '4':
            display_tenants()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def main():
    property_management_menu()

if __name__ == "__main__":
    main()
