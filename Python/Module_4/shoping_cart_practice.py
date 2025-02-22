"""
Products- name, price, stock
Customers- name
CartItems- products, quantity
Cart- User, CartItems
PaymentMethod- Paypal, Creditcard

"""

# Create products
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name}=${self.price}-{self.stock}"

# Create Customer
class Customer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name  # human readable string er jonno

# Create CartItems
# cartItems holo ekta cart er vitor joto gula products thake
class CartItems:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        if quantity > product.stock:
            print("Not available")

    def get_total_price(self):
        return self.product.price * self.quantity

# Create Cart
class Cart:
    def __init__(self, customer):
        self.customer = customer
        self.cart = []

    def add_to_cart(self, product, quantity):  # load cart items(item beshi thakle setau add korte hobe)
        self.cart.append(CartItems(product, quantity))

    def calculate_total(self):
        total_price = 0
        for item in self.cart:
            total_price += item.get_total_price()
        return total_price

    def display_cart(self):
        print(f"Shopping cart of {self.customer}")

        for item in self.cart:
            print(f"{item.product.name} x {item.quantity} - ${item.get_total_price()}")

        print(f"Total: $ {self.calculate_total()}")

coke = Product("Coca-Cola", 80, 1)
glucose = Product("Glucose", 150, 15)

customer_name = input()
user = Customer(customer_name)
user_cart = Cart(user)

user_cart.add_to_cart(coke, 2)
user_cart.add_to_cart(glucose, 1)

user_cart.display_cart()



