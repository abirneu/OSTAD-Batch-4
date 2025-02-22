# Product - name,price,stock
# Customer - name
# CartItems - product+quantity
# Cart - User, CartItems

# PaymentMthod (Paypal,CreditCart)

# 1.Create Product class


class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.__stock = stock

    def __str__(self):
        return f"{self.name}-${self.price}-{self.__stock}"
    
# Create Customer
class Customer:
    def __init__(self,name):
        self.name = name

    
    def __str__(self):
        return self.name

class CartItems:
    def __init__(self,product,quantity):
        self.product = product
        self.quantity = quantity

    def get_total_price(self):
        return self.product.price * self.quantity

class Cart:
    def __init__(self,customer):
        self.customer = customer
        self.cart = []
    
    def add_to_cart(self,product,quantity):
        self.cart.append(CartItems(product,quantity))

    
    def calculate_total(self):
        total_price = 0

        for item in self.cart:
           total_price += item.get_total_price()
        
        return total_price
    
    def display_cart(self):
        print(f'Sopping Cart of {self.customer}')

        for item in self.cart:
            print(f"{item.product.name} x {item.quantity} - ${item.get_total_price()}")

        print(f"Total: $ {self.calculate_total()}")
    
from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay():
        pass

class CreditCard(Payment):
    def pay(self,amount):
        print(f"Paid ${amount} using creadit card")

class PayPalCard(Payment):
    def pay(self,amount):
        print(f"Paid ${amount} using PayPal")


laptop = Product('laptop',10000,10)
phone = Product('Iphone',20000,20)

customer_name = input()
abdur = Customer(customer_name)

abdur_cart = Cart(abdur)

abdur_cart.add_to_cart(laptop,2)
abdur_cart.add_to_cart(phone,1)

abdur_cart.display_cart()

# credit_card = CreditCard()
# credit_card.pay(abdur_cart.calculate_total())

paypal = PayPalCard()
paypal.pay(abdur_cart.calculate_total())