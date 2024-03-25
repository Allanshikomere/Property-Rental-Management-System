from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Property(Base):
    __tablename__ = 'properties'

    id = Column(Integer, primary_key=True)
    address = Column(String)
    

class Tenant(Base):
    __tablename__ = 'tenants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    property_id = Column(Integer, ForeignKey('properties.id'))


engine = create_engine('sqlite:///property_rental_management.db')
Base.metadata.create_all(engine)  
Session = sessionmaker(bind=engine)

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

def display_available_tenants():
    session = Session()
    try:
        tenants = session.query(Tenant).filter(Tenant.property_id.is_(None)).all()
        if tenants:
            print("===== Available Tenants List =====")
            for tenant in tenants:
                print(f"ID: {tenant.id}, Name: {tenant.name}")
        else:
            print("No available Tenants found.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
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


if __name__ == "__main__":
    tenant_management_menu()
