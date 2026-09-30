# Functions for calculating and printing the bill

def calculate_subtotal(products, cart):
    total = 0

    for product_id in cart:
        total += products[product_id]["price"] * cart[product_id]

    return total


def calculate_discount(subtotal):
    if subtotal >= 2000:
        return subtotal * 0.10
    elif subtotal >= 1000:
        return subtotal * 0.05
    else:
        return 0


def generate_bill(products, cart):
    if len(cart) == 0:
        print("\nCart is empty. Add products before generating a bill.")
        return 0

    subtotal = calculate_subtotal(products, cart)
    discount = calculate_discount(subtotal)
    final_total = subtotal - discount

    print("\n" + "=" * 72)
    print("                         CUSTOMER BILL")
    print("=" * 72)
    print(f"{'PRODUCT':<25}{'QTY':>8}{'PRICE':>15}{'AMOUNT':>15}")
    print("-" * 72)

    for product_id in cart:
        item = products[product_id]
        quantity = cart[product_id]
        amount = item["price"] * quantity
        print(f"{item['name']:<25}{quantity:>8}₹{item['price']:>13.2f}₹{amount:>13.2f}")

    print("-" * 72)
    print(f"{'Subtotal':>55} ₹{subtotal:>10.2f}")
    print(f"{'Discount':>55} ₹{discount:>10.2f}")
    print(f"{'Final Total':>55} ₹{final_total:>10.2f}")
    print("=" * 72)

    # Update inventory after a successful bill.
    for product_id in cart:
        products[product_id]["stock"] -= cart[product_id]

    cart.clear()
    print("Bill created. Stock has been updated.")
    return final_total
