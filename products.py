# Functions for displaying and searching products

def display_products(products):
    print("\n" + "=" * 68)
    print(f"{'ID':<8}{'PRODUCT':<22}{'PRICE':>12}{'STOCK':>12}")
    print("=" * 68)

    if len(products) == 0:
        print("No products available.")
    else:
        for product_id in sorted(products):
            item = products[product_id]
            print(f"{product_id:<8}{item['name']:<22}₹{item['price']:>10.2f}{item['stock']:>12}")

    print("=" * 68)


def search_product(products, product_id):
    if product_id in products:
        return products[product_id]
    return None


def search_by_name(products, keyword):
    matches = []
    keyword = keyword.lower()

    for product_id in products:
        if keyword in products[product_id]["name"].lower():
            matches.append(product_id)

    return matches


def sorted_product_ids(products, option):
    ids = list(products.keys())

    if option == 1:
        ids.sort()
    elif option == 2:
        ids.sort(key=lambda x: products[x]["name"])
    elif option == 3:
        ids.sort(key=lambda x: products[x]["price"])
    elif option == 4:
        ids.sort(key=lambda x: products[x]["stock"])

    return ids


def display_sorted_products(products, option):
    ids = sorted_product_ids(products, option)

    print("\n" + "=" * 68)
    print(f"{'ID':<8}{'PRODUCT':<22}{'PRICE':>12}{'STOCK':>12}")
    print("=" * 68)

    for product_id in ids:
        item = products[product_id]
        print(f"{product_id:<8}{item['name']:<22}₹{item['price']:>10.2f}{item['stock']:>12}")

    print("=" * 68)
