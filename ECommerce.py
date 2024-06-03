class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Stock: {self.stock}"


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
        else:
            print("Product not found in inventory.")

    def view_products(self):
        for product in self.products.values():
            print(product)


class Cart:
    def __init__(self):
        self.products = {}

    def add_to_cart(self, product, quantity):
        if product.product_id in self.products:
            self.products[product.product_id]['quantity'] += quantity
        else:
            self.products[product.product_id] = {'product': product, 'quantity': quantity}

    def remove_from_cart(self, product_id, quantity):
        if product_id in self.products:
            if self.products[product_id]['quantity'] <= quantity:
                del self.products[product_id]
            else:
                self.products[product_id]['quantity'] -= quantity
        else:
            print("Product not found in cart.")

    def view_cart(self):
        for item in self.products.values():
            product = item['product']
            quantity = item['quantity']
            print(f"Product: {product.name}, Quantity: {quantity}, Total Price: {product.price * quantity}")

    def checkout(self):
        total = 0
        for item in self.products.values():
            product = item['product']
            quantity = item['quantity']
            if product.stock >= quantity:
                product.stock -= quantity
                total += product.price * quantity
            else:
                print(f"Insufficient stock for product: {product.name}")
        self.products.clear()
        print(f"Total amount to be paid: {total}")


def main():
    inventory = Inventory()
    cart = Cart()

    # Adding some products to the inventory
    inventory.add_product(Product(1, "Laptop", 1000, 10))
    inventory.add_product(Product(2, "Smartphone", 500, 20))
    inventory.add_product(Product(3, "Tablet", 300, 15))

    while True:
        print("\n1. View Products\n2. Add to Cart\n3. View Cart\n4. Remove from Cart\n5. Checkout\n6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            inventory.view_products()
        elif choice == 2:
            product_id = int(input("Enter product ID to add to cart: "))
            quantity = int(input("Enter quantity: "))
            if product_id in inventory.products:
                product = inventory.products[product_id]
                if product.stock >= quantity:
                    cart.add_to_cart(product, quantity)
                else:
                    print("Insufficient stock.")
            else:
                print("Product not found.")
        elif choice == 3:
            cart.view_cart()
        elif choice == 4:
            product_id = int(input("Enter product ID to remove from cart: "))
            quantity = int(input("Enter quantity: "))
            cart.remove_from_cart(product_id, quantity)
        elif choice == 5:
            cart.checkout()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
