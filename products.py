class Product:
    """
    Represents a product in an electronics store.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a Product instance.

        Args:
            name (str): The name of the product. Cannot be empty.
            price (float): The price of the product. Must be non-negative.
            quantity (int): The available quantity of the product. Must be non-negative.

        Raises:
            ValueError: If the name is empty, or if price or quantity are negative.
        """
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Product price cannot be negative.")
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """
        Returns the current quantity of the product.

        Returns:
            int: The available quantity.
        """
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Sets the quantity of the product.

        If the quantity is set to 0, the product is automatically deactivated.

        Args:
            quantity (int): The new quantity. Must be non-negative.

        Raises:
            ValueError: If the provided quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be set to a negative number.")

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Checks if the product is active.

        Returns:
            bool: True if the product is active, False otherwise.
        """
        return self.active

    def activate(self):
        """
        Activates the product, making it available for purchase.
        """
        self.active = True
        print(f"{self.name} has been activated.")

    def deactivate(self):
        """
        Deactivates the product, making it unavailable for purchase.
        """
        self.active = False
        print(f"{self.name} has been deactivated.")

    def show(self) -> str:
        """
        Returns a string representation of the product.

        Returns:
            str: A formatted string with product details.
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Processes a purchase of a given quantity of the product.

        Args:
            quantity (int): The number of items to buy.

        Returns:
            float: The total price of the purchase.

        Raises:
            ValueError: If the product is inactive, the purchase quantity is not positive,
                        or if there is not enough stock.
        """
        if not self.is_active():
            raise ValueError(f"Cannot buy {self.name} as it is currently inactive.")

        if quantity <= 0:
            raise ValueError("Purchase quantity must be a positive number.")

        if quantity > self.quantity:
            raise ValueError(f"Not enough stock for {self.name}. "
                             f"Available: {self.quantity}, Requested: {quantity}")

        # Calculate total price
        total_price = quantity * self.price

        # Update the quantity
        self.set_quantity(self.quantity - quantity)

        print(f"Purchase successful! Total for {quantity} of {self.name}: ${total_price:.2f}")
        return total_price


# --- Example Usage ---
if __name__ == "__main__":
    try:
        # Create a product
        macbook = Product("MacBook Air M2", 1450.00, 100)
        print(macbook.show())
        print(f"Is active? {macbook.is_active()}")
        print("-" * 20)

        # Buy some
        macbook.buy(5)
        print(macbook.show())
        print("-" * 20)

        # Buy the rest
        macbook.buy(95)
        print(macbook.show())
        print(f"Is active? {macbook.is_active()}")
        print("-" * 20)

        # Try to buy more (should fail)
        try:
            macbook.buy(1)
        except ValueError as e:
            print(f"Error: {e}")
        print("-" * 20)

        # Manually reactivate and restock
        macbook.activate()
        macbook.set_quantity(50)
        print(macbook.show())
        print(f"Is active? {macbook.is_active()}")
        print("-" * 20)

        # Try to create an invalid product (should fail)
        try:
            invalid_product = Product("", -100, -5)
        except ValueError as e:
            print(f"Error creating product: {e}")

    except ValueError as e:
        print(f"An error occurred: {e}")
