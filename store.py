from typing import List, Tuple
from products import Product


class Store:
    """
    Represents a store that holds and manages a collection of products.
    """

    def __init__(self, products: List[Product]):
        """
        Initializes a Store instance.

        Args:
            products (List[Product]): A list of Product objects to stock the store with.
        """
        if not isinstance(products, list):
            raise TypeError("Input products must be a list.")
        for product in products:
            if not isinstance(product, Product):
                raise TypeError(
                    "All items in the list must be of type Product.")
        self.products = products

    def add_product(self, product: Product):
        """
        Adds a product to the store.
        """
        if not isinstance(product, Product):
            raise TypeError("Input product must be of type Product.")
        self.products.append(product)
        print(f"Added {product.name} to the store.")

    def remove_product(self, product: Product):
        """
        Removes a product from the store.
        """
        if not isinstance(product, Product):
            raise TypeError("Input product must be of type Product.")
        if product in self.products:
            self.products.remove(product)
            print(f"Removed {product.name} from the store.")
        else:
            print(f"{product.name} not found in the store.")

    def get_total_quantity(self) -> int:
        """
        Returns the total number of all items in the store.
        """
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    def get_all_products(self) -> List[Product]:
        """
        Returns a list of all active products in the store.
        """
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Processes an order for multiple products.

        Args:
            shopping_list: A list of tuples, where each tuple contains a Product
                           object and the integer quantity to order.

        Returns:
            The total price of the order (float).
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            try:
                purchase_price = product.buy(quantity)
                total_price += purchase_price
                print(f"Purchased {quantity} of {product.name}.")
            except ValueError as exception_value:
                print(f"Order failed for {product.name}: {exception_value}")
                # Depending on requirements, you might want to stop the whole order
                # or just skip the failed item. Here we skip it.

        return total_price
