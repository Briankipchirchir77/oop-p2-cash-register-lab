# Cash Register Lab

A Python implementation of a cash register for an e-commerce site, built using Object Oriented Programming (OOP) principles.

## Description

This project simulates a cash register that can:
- Add items with prices and quantities
- Apply percentage discounts to the total
- Void the last transaction

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Briankipchirchir77/oop-p2-cash-register-lab.git
```

2. Navigate into the project:
```bash
cd oop-p2-cash-register-lab
```

3. Install dependencies:
```bash
npm install
```

## Usage

```python
from cash_register import CashRegister

# Create a register with 20% discount
register = CashRegister(20)

# Add items
register.add_item("Apple", 1.50, 3)
register.add_item("Bread", 2.00)

# Apply discount
register.apply_discount()

# Void last transaction
register.void_last_transaction()
```

## CashRegister Class

| Attribute | Description |
|---|---|
| `discount` | percentage off total (0-100) |
| `total` | running total of all items |
| `items` | list of all added items |
| `previous_transactions` | list of all transactions |

| Method | Description |
|---|---|
| `add_item(item, price, quantity)` | adds item to register |
| `apply_discount()` | applies discount to total |
| `void_last_transaction()` | removes last transaction |

## Running Tests

```bash
pytest
```

All 14 tests should pass:
## Screenshot

![Passing Tests](screenshot.png)