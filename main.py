from store import Store
from products import Product

def start(store: Store):
    """
    Runs the main user interface loop for the store.
    """
    while True:
        print("\n--- Store Menu ---")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            print("\n--- All Products ---")
            products = store.get_all_products()
            if not products:
                print("No active products in store.")
            for i, product in enumerate(products, 1):
                print(f"{i}. {product.show()}")

        elif choice == "2":
            total_quantity = store.get_total_quantity()
            print(f"\nTotal items in store: {total_quantity}")

        elif choice == "3":
            print("\n--- Make an Order ---")
            products = store.get_all_products()
            if not products:
                print("Store is empty, cannot place an order.")
                continue

            for i, product in enumerate(products, 1):
                print(f"{i}. {product.show()}")

            shopping_list = []
            while True:
                product_choice = input("Which product # do you want? (or 'done' to finish): ")
                if product_choice.lower() == 'done':
                    break

                try:
                    product_index = int(product_choice) - 1
                    if not 0 <= product_index < len(products):
                        print("Invalid product number.")
                        continue

                    quantity_choice = input("What quantity do you want?: ")
                    quantity = int(quantity_choice)

                    chosen_product = products[product_index]
                    shopping_list.append((chosen_product, quantity))
                    print("Product added to order.")

                except ValueError:
                    print("Invalid input. Please enter numbers for product and quantity.")

            if shopping_list:
                total_cost = store.order(shopping_list)
                print(f"\nOrder complete! Total cost: ${total_cost:.2f}")

        elif choice == "4":
            print("Bye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


# This is the main execution block
if __name__ == "__main__":
    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    Product("Sony PlayStation 5", price=499.99, quantity=0)  # Inactive product
                    ]
    best_buy = Store(product_list)

    # Start the user interface
    start(best_buy)
