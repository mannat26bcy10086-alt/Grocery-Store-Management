# Smart Grocery Store Inventory & Billing System

## Overview
Smart Grocery Store is a console-based Python project for managing grocery products, a customer shopping cart, billing, and inventory analysis.

The project is designed using basic Python programming concepts such as variables, input/output, conditional statements, loops, functions, lists, dictionaries, indexing, searching, sorting, and arithmetic operations.

## Major Functional Modules

1. Inventory Management
   - View products
   - Add products
   - Update prices and stock
   - Remove products
   - Search products

2. Shopping Cart & Billing
   - Add products to cart
   - Remove products from cart
   - View cart
   - Generate bill
   - Apply discount
   - Update inventory after billing

3. Inventory & Sales Analysis
   - Total stock
   - Inventory value
   - Lowest stock item
   - Highest priced item
   - Low-stock report
   - Sorting report

## Technologies
- Python 3
- Python built-in data structures
- No external packages required

## Project Structure

Smart-Grocery-Store/
├── main.py
├── data.py
├── products.py
├── inventory.py
├── cart.py
├── billing.py
├── analysis.py
├── validation.py
├── README.md
├── statement.md
├── sample_output.txt
├── tests/
│   └── test_project.py
└── docs/

## How to Run

1. Install Python 3.
2. Open a terminal in the project folder.
3. Run:

```bash
python main.py
```

## How to Test

Run:

```bash
python tests/test_project.py
```

Expected result:

```text
All tests passed successfully.
```

## Input / Output

Inputs include product IDs, product names, prices, quantities and menu choices.

Outputs include product tables, shopping-cart details, bills, inventory statistics and sorting reports.

## Syllabus Alignment

The project uses:
- Variables and expressions
- Strings and numeric data
- Lists and dictionaries
- Indexing and list processing
- Conditional statements
- For and while loops
- Functions and parameters
- Searching and sorting
- Basic problem-solving algorithms
- Input validation

## Future Enhancements
- Persistent file storage
- Customer accounts
- Barcode support
- Graphical user interface
- Database integration
