# Inventory and sales analysis module

def inventory_value(products):
    total = 0

    for product_id in products:
        total += products[product_id]["price"] * products[product_id]["stock"]

    return total


def total_stock(products):
    total = 0

    for product_id in products:
        total += products[product_id]["stock"]

    return total


def lowest_stock_product(products):
    if len(products) == 0:
        return None

    ids = list(products.keys())
    lowest_id = ids[0]

    for product_id in ids[1:]:
        if products[product_id]["stock"] < products[lowest_id]["stock"]:
            lowest_id = product_id

    return lowest_id


def highest_price_product(products):
    if len(products) == 0:
        return None

    ids = list(products.keys())
    highest_id = ids[0]

    for product_id in ids[1:]:
        if products[product_id]["price"] > products[highest_id]["price"]:
            highest_id = product_id

    return highest_id


def low_stock_products(products, limit=10):
    result = []

    for product_id in products:
        if products[product_id]["stock"] <= limit:
            result.append(product_id)

    return result


def analysis_report(products):
    print("\n" + "=" * 68)
    print("                      STOCK REPORT")
    print("=" * 68)

    if len(products) == 0:
        print("No products available.")
        return

    total_products = len(products)
    units = total_stock(products)
    value = inventory_value(products)

    low_id = lowest_stock_product(products)
    high_id = highest_price_product(products)

    print(f"Number of products    : {total_products}")
    print(f"Total items in stock  : {units}")
    print(f"Value of stock        : ₹{value:.2f}")

    print(f"Least available item  : {products[low_id]['name']} ({products[low_id]['stock']} units)")
    print(f"Costliest product     : {products[high_id]['name']} (₹{products[high_id]['price']:.2f})")

    low_items = low_stock_products(products)

    print("\nProducts which may need restocking:")
    if len(low_items) == 0:
        print("None")
    else:
        for product_id in low_items:
            print(f"- {products[product_id]['name']} : {products[product_id]['stock']} units")

    print("=" * 68)


def sorting_report(products):
    print("\n========== SORTING REPORT ==========")
    print("1. Sort by name")
    print("2. Sort by price")
    print("3. Sort by stock")

    choice = input("Enter choice: ")

    ids = list(products.keys())

    if choice == "1":
        ids.sort(key=lambda x: products[x]["name"])
    elif choice == "2":
        ids.sort(key=lambda x: products[x]["price"])
    elif choice == "3":
        ids.sort(key=lambda x: products[x]["stock"])
    else:
        print("Invalid choice.")
        return

    for position in range(len(ids)):
        product_id = ids[position]
        item = products[product_id]
        print(f"{position + 1}. {item['name']} - ₹{item['price']:.2f} - Stock: {item['stock']}")
