from sqlalchemy.orm import sessionmaker
from models import Tenant, Property
from db import engine

Session = sessionmaker(bind=engine)

def add_tenant():
    session = Session()
    
    # Get tenant name
    name = input("Enter tenant name: ")

    # Get property ID and validate
    while True:
        property_id = input("Enter property ID: ")
        property = session.query(Property).filter_by(id=property_id).first()
        if property:
            break  # Valid property ID, exit the loop
        else:
            print("Error: Property ID does not exist. Please enter a valid property ID.")

    # Create tenant instance and add to session
    tenant = Tenant(name=name, property_id=property_id)
    session.add(tenant)
    session.commit()
    print("Tenant added successfully.")
    session.close()

def display_available_tenants():
    session = Session()
    tenants = session.query(Tenant).filter(Tenant.property_id.is_(None)).all()
    if tenants:
        print("===== Available Tenants List =====")
        for tenant in tenants:
            print(f"ID: {tenant.id}, Name: {tenant.name}")
    else:
        print("No available tenants found.")
    session.close()

def tenant_management_menu():
    while True:
        print("===== Tenant Management Menu =====")
        print("1. Add Tenant")
        print("2. Display Available Tenants")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_tenant()
        elif choice == '2':
            display_available_tenants()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a valid option.")
