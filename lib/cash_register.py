# Cash Register class for an e-commerce site
class CashRegister:
    """
    A class to simulate a cash register for an e-commerce site.
    Supports adding items, applying discounts, and voiding transactions.
    """

    def __init__(self, discount=0):
        """
        Initialize the cash register.
        discount: optional percentage off (0-100). Defaults to 0.
        """
        self._discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        """Getter for discount."""
        return self._discount

    @discount.setter
    def discount(self, value):
        """
        Validates discount is an integer between 0 and 100.
        """
        if not isinstance(value, int) or not (0 <= value <= 100):
            print("Not valid discount")
            self._discount = 0
        else:
            self._discount = value

    def add_item(self, item, price, quantity=1):
        """
        Add an item to the cash register.
        item: name of the item
        price: price per single item
        quantity: how many (defaults to 1)
        """
        # Calculate total price for this item
        item_total = price * quantity

        # Add to running total
        self.total += item_total

        # Add item name to items list (once per quantity)
        for _ in range(quantity):
            self.items.append(item)

        # Record transaction
        self.previous_transactions.append({
            'item': item,
            'price': item_total,
            'quantity': quantity
        })

    def apply_discount(self):
        """
        Apply the discount percentage to the current total.
        Prints error message if no discount is set.
        """
        if self._discount == 0:
            print("There is no discount to apply.")
            return

        # Calculate and apply discount
        discount_amount = (self._discount / 100) * self.total
        self.total -= discount_amount

        print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        """
        Remove the last transaction.
        Adjusts total and items list accordingly.
        """
        if not self.previous_transactions:
            print("There are no transactions to void.")
            return

        # Pop last transaction
        last = self.previous_transactions.pop()

        # Subtract from total
        self.total -= last['price']

        # Remove items from items list
        for _ in range(last['quantity']):
            self.items.remove(last['item'])

    def __repr__(self):
        """String representation of the cash register."""
        return (f"CashRegister | Total: ${self.total} | "
                f"Items: {self.items} | Discount: {self._discount}%")