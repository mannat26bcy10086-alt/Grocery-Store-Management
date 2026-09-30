# Smart Grocery Store Inventory & Billing System
# Main program

from data import products
from inventory import inventory_menu
from cart import cart_menu
from billing import generate_bill
from analysis import analysis_report, sorting_report


def show_menu():
    print("\n" + "=" * 68)
    print("           GROCERY STORE MANAGEMENT")
    print("=" * 68)
    print("1. Manage Products")
    print("2. Customer Cart")
    print("3. Make Bill")
    print("4. Check Stock Report")
    print("5. Sort Products")
    print("6. Exit")
    print("=" * 68)


def main():
    cart = {}

    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            inventory_menu(products)
        elif choice == "2":
            cart_menu(products, cart)
        elif choice == "3":
            generate_bill(products, cart)
        elif choice == "4":
            analysis_report(products)
        elif choice == "5":
            sorting_report(products)
        elif choice == "6":
            print("\nThank you for using Smart Grocery Store System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
