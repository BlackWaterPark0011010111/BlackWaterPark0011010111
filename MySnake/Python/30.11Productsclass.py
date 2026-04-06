class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"ID product: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price} doll.")
        print(f"Quantity: {self.quantity} stk.")

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_id):
        self.products = [p for p in self.products if p.product_id != product_id]

    def display_inventory(self):
        print("Inventory:")
        for product in self.products:
            product.display_info()
            print("------------------------")

    def find_product_by_id(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None
    



product1 = Product(1, 'Laptop', 1200, 10)
product2 = Product(2, "Mouse", 20, 50)
product3 = Product(3, "Keyboard", 50, 30)

# Creating inventory
inventory = Inventory()

# Adding products to the inventory
inventory.add_product(product1)
inventory.add_product(product2)
inventory.add_product(product3)

# Displaying the initial inventory
inventory.display_inventory()

# Finding and updating quantity of a product
found_product = inventory.find_product_by_id(1)
if found_product:
    found_product.update_quantity(5)

# Removing a product from the inventory
inventory.remove_product(2)

# Displaying the updated inventory
inventory.display_inventory()