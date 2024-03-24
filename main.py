from property_management import property_management_menu
from tenant_management import tenant_management_menu, display_available_tenants
from under_construction_management import under_construction_property_management_menu

def main_menu():
    print("===== Property Rental Management System =====")
    print("1. Property Management")
    print("2. Tenant Management")
    print("3. Under Construction Property Management")
    print("4. Display Available Tenants")
    print("5. Exit")

def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            property_management_menu()
        elif choice == '2':
            tenant_management_menu()
        elif choice == '3':
            under_construction_property_management_menu()
        elif choice == '4':
            display_available_tenants()
        elif choice == '5':
            print("Exiting Property Rental Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
