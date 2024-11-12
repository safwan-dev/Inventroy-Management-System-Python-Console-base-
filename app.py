class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Price: ${self.price:.2f}, Stock: {self.stock_quantity}"

class InventoryManagementSystem:
    def __init__(self):
        self.users = [
            User("admin", "admin123", "Admin"),
            User("user", "user123", "User")
        ]
        self.products = {}
        self.current_user = None
        self.low_stock_threshold = 5

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        for user in self.users:
            if user.username == username and user.password == password:
                self.current_user = user
                print(f"Login successful! Welcome, {user.role}.")
                return True
        print("Invalid username or password.")
        return False

    def add_product(self):
        try:
            product_id = input("Enter product ID: ")
            if product_id in self.products:
                print("Product ID already exists.")
                return

            name = input("Enter product name: ")
            category = input("Enter product category: ")
            price = float(input("Enter product price: "))
            stock_quantity = int(input("Enter stock quantity: "))

            product = Product(product_id, name, category, price, stock_quantity)
            self.products[product_id] = product
            print("Product added successfully.")
        except ValueError:
            print("Invalid input. Please enter valid price and stock quantity.")

    def edit_product(self):
        product_id = input("Enter product ID to edit: ")
        if product_id not in self.products:
            print("Product not found.")
            return

        product = self.products[product_id]
        print(f"Editing product: {product}")
        try:
            product.name = input("Enter new name: ") or product.name
            product.category = input("Enter new category: ") or product.category
            product.price = float(input("Enter new price: ")) or product.price
            product.stock_quantity = int(input("Enter new stock quantity: ")) or product.stock_quantity
            print("Product updated successfully.")
        except ValueError:
            print("Invalid input. Please enter valid price and stock quantity.")

    def delete_product(self):
        product_id = input("Enter product ID to delete: ")
        if product_id in self.products:
            del self.products[product_id]
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    def view_products(self):
        if not self.products:
            print("No products in inventory.")
            return

        for product in self.products.values():
            print(product)
            if product.stock_quantity < self.low_stock_threshold:
                print("Warning: Low stock. Consider restocking.")

    def search_product(self):
        search_term = input("Enter product name or category to search: ").lower()
        found = False
        for product in self.products.values():
            if search_term in product.name.lower() or search_term in product.category.lower():
                print(product)
                found = True
        if not found:
            print("No matching products found.")

    def adjust_stock(self):
        product_id = input("Enter product ID to adjust stock: ")
        if product_id not in self.products:
            print("Product not found.")
            return

        try:
            adjustment = int(input("Enter stock adjustment (positive to add, negative to reduce): "))
            self.products[product_id].stock_quantity += adjustment
            print("Stock adjusted successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def start(self):
        if not self.login():
            return

        while True:
            print("\nOptions:")
            print("1. View Products")
            if self.current_user.role == "Admin":
                print("2. Add Product")
                print("3. Edit Product")
                print("4. Delete Product")
            print("5. Search Product")
            print("6. Adjust Stock")
            print("0. Logout")

            choice = input("Choose an option: ")
            if choice == "1":
                self.view_products()
            elif choice == "2" and self.current_user.role == "Admin":
                self.add_product()
            elif choice == "3" and self.current_user.role == "Admin":
                self.edit_product()
            elif choice == "4" and self.current_user.role == "Admin":
                self.delete_product()
            elif choice == "5":
                self.search_product()
            elif choice == "6":
                self.adjust_stock()
            elif choice == "0":
                print("Logging out.")
                break
            else:
                print("Invalid option or insufficient privileges.")

if __name__ == "__main__":
    system = InventoryManagementSystem()
    system.start()
