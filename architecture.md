# System Architecture

The project follows a simple modular console architecture.

User
  |
  v
main.py
  |
  +--> inventory.py --> products.py
  |
  +--> cart.py -------> products.py
  |
  +--> billing.py ----> products.py
  |
  +--> analysis.py ---> products.py
  |
  +--> validation.py
  |
  v
Console Output

Data is maintained using Python dictionaries, lists and tuples where appropriate.
