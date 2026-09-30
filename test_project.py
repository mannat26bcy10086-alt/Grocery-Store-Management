# Basic validation tests for the project

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from data import products
from billing import calculate_subtotal, calculate_discount
from analysis import total_stock, inventory_value, low_stock_products


def test_subtotal():
    cart = {101: 2, 102: 3}
    assert calculate_subtotal(products, cart) == 210.0


def test_discount_below_1000():
    assert calculate_discount(500) == 0


def test_discount_1000():
    assert calculate_discount(1000) == 50


def test_total_stock():
    assert total_stock(products) == 195


def test_inventory_value():
    expected = sum(item["price"] * item["stock"] for item in products.values())
    assert inventory_value(products) == expected


def test_low_stock():
    result = low_stock_products(products, 15)
    assert 104 in result
    assert 107 in result


if __name__ == "__main__":
    test_subtotal()
    test_discount_below_1000()
    test_discount_1000()
    test_total_stock()
    test_inventory_value()
    test_low_stock()
    print("All tests passed successfully.")
