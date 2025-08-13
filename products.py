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
        if not isinstance(name, str):
            raise TypeError("Product name must be a string.")
        if not isinstance(price, float):
            raise TypeError("Product price must be a float.")
        if not isinstance(quantity, int):
            raise TypeError("Product quantity must be an integer.")
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Product price cannot be negative.")
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0

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
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
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
        if not isinstance(quantity, int):
            raise TypeError("Purchase quantity must be an integer.")
        if not self.is_active():
            raise ValueError(
                f"Cannot buy {self.name} as it is currently inactive.")

        if quantity <= 0:
            raise ValueError("Purchase quantity must be a positive number.")

        if quantity > self.quantity:
            raise ValueError(f"Not enough stock for {self.name}. "
                             f"Available: {self.quantity}, Requested: {quantity}")

        # Calculate total price
        total_price = quantity * self.price

        # Update the quantity
        self.set_quantity(self.quantity - quantity)

        print(
            f"Purchase successful! Total for {quantity} of {self.name}: ${total_price:.2f}")
        return total_price
