# Functions used for the customer's cart

from validation import get_positive_integer


def add_to_cart(products, cart):
    print("\n--- Add to Cart ---")
    product_id = get_positive_integer("Enter product ID: ")

    if product_id not in products:
        print("Product not found.")
        return

    quantity = get_positive_integer("Enter quantity: ")

    current_quantity = cart.get(product_id, 0)
    available = products[product_id]["stock"]

    if current_quantity + quantity > available:
        print(f"Only {available - current_quantity} more unit(s) available.")
        return

    cart[product_id] = current_quantity + quantity
    print(f"{quantity} x {products[product_id]['name']} added to cart.")


def remove_from_cart(products, cart):
    print("\n--- Remove from Cart ---")
    product_id = get_positive_integer("Enter product ID: ")

    if product_id not in cart:
        print("Product is not in the cart.")
        return

    del cart[product_id]
    print("Item removed from cart.")


def view_cart(products, cart):
    print("\n" + "=" * 68)
    print("                         SHOPPING CART")
    print("=" * 68)

    if len(cart) == 0:
        print("Cart is empty.")
        print("=" * 68)
        return

    print(f"{'PRODUCT':<25}{'QTY':>8}{'PRICE':>15}{'AMOUNT':>15}")
    print("-" * 68)

    for product_id in cart:
        item = products[product_id]
        quantity = cart[product_id]
        amount = quantity * item["price"]
        print(f"{item['name']:<25}{quantity:>8}₹{item['price']:>13.2f}₹{amount:>13.2f}")

    print("=" * 68)


def cart_menu(products, cart):
    while True:
        print("\n========== CUSTOMER CART ==========")
        print("1. Add to Cart")
        print("2. Remove from Cart")
        print("3. View Cart")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            add_to_cart(products, cart)
        elif choice == "2":
            remove_from_cart(products, cart)
        elif choice == "3":
            view_cart(products, cart)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
