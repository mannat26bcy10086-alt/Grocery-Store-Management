# Inventory management module

from validation import get_positive_integer, get_positive_float
from products import display_products, search_by_name


def add_product(products):
    print("\n--- Add New Product ---")
    product_id = get_positive_integer("Enter product ID: ")

    if product_id in products:
        print("Product ID already exists.")
        return

    name = input("Enter product name: ").strip()
    while name == "":
        print("Product name cannot be empty.")
        name = input("Enter product name: ").strip()

    price = get_positive_float("Enter price: ")
    stock = get_positive_integer("Enter stock quantity: ")

    products[product_id] = {
        "name": name,
        "price": price,
        "stock": stock
    }

    print("Product added successfully.")


def update_product(products):
    print("\n--- Change Product Details ---")
    product_id = get_positive_integer("Enter product ID: ")

    if product_id not in products:
        print("Product not found.")
        return

    print("1. Update price")
    print("2. Update stock")
    choice = input("Enter choice: ")

    if choice == "1":
        products[product_id]["price"] = get_positive_float("Enter new price: ")
        print("Price updated successfully.")
    elif choice == "2":
        products[product_id]["stock"] = get_positive_integer("Enter new stock: ")
        print("Stock updated successfully.")
    else:
        print("Invalid choice.")


def remove_product(products):
    print("\n--- Delete Product ---")
    product_id = get_positive_integer("Enter product ID: ")

    if product_id in products:
        del products[product_id]
        print("Product removed successfully.")
    else:
        print("Product not found.")


def find_product(products):
    print("\n--- Find Product ---")
    print("1. Search by ID")
    print("2. Search by name")
    choice = input("Enter choice: ")

    if choice == "1":
        product_id = get_positive_integer("Enter product ID: ")
        if product_id in products:
            item = products[product_id]
            print(f"ID: {product_id}")
            print(f"Name: {item['name']}")
            print(f"Price: ₹{item['price']:.2f}")
            print(f"Stock: {item['stock']}")
        else:
            print("Product not found.")

    elif choice == "2":
        keyword = input("Enter product name/keyword: ").strip()
        matches = search_by_name(products, keyword)

        if len(matches) == 0:
            print("No matching products found.")
        else:
            for product_id in matches:
                item = products[product_id]
                print(f"{product_id} - {item['name']} - ₹{item['price']:.2f} - Stock: {item['stock']}")
    else:
        print("Invalid choice.")


def inventory_menu(products):
    while True:
        print("\n========== MANAGE PRODUCTS ==========")
        print("1. Show All Products")
        print("2. Add New Product")
        print("3. Change Product Details")
        print("4. Delete Product")
        print("5. Find Product")
        print("6. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            display_products(products)
        elif choice == "2":
            add_product(products)
        elif choice == "3":
            update_product(products)
        elif choice == "4":
            remove_product(products)
        elif choice == "5":
            find_product(products)
        elif choice == "6":
            break
        else:
            print("Invalid choice.")
