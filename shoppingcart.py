class Fruit:
    def __init__(self, name, price_per_unit):
        self.name = name
        self.price_per_unit = price_per_unit

    def get_price(self, quantity):
        return self.price_per_unit * quantity

    def __str__(self):
        return f"{self.name} (${self.price_per_unit}/unit)"

class ShoppingCart:
    def __init__(self):
        self.items = {} 

    def add_item(self, fruit, quantity):
        if not isinstance(fruit, Fruit):
            raise TypeError("Only Fruit objects can be added to the cart.")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive number.")
        
        if fruit in self.items:
            self.items[fruit] += quantity
        else:
            self.items[fruit] = quantity
        print(f"Added {quantity} {fruit.name}(s) to the cart.")

    def remove_item(self, fruit, quantity=None):
        if fruit not in self.items:
            print(f"{fruit.name} is not in the cart.")
            return

        if quantity is None or quantity >= self.items[fruit]:
            del self.items[fruit]
            print(f"Removed all {fruit.name}(s) from the cart.")
        else:
            self.items[fruit] -= quantity
            print(f"Removed {quantity} {fruit.name}(s) from the cart.")

    def calculate_total(self):
        total_price = 0
        for fruit, quantity in self.items.items():
            total_price += fruit.get_price(quantity)
        return total_price

    def display_cart(self):
        if not self.items:
            print("Your shopping cart is empty.")
            return

        print("\n--- Your Shopping Cart ---")
        for fruit, quantity in self.items.items():
            item_total = fruit.get_price(quantity)
            print(f"{fruit.name}: {quantity} units - {item_total:.2f}")
        print(f"--------------------------")
        print(f"Total: {self.calculate_total():.2f}")

apple = Fruit("Apple", 1.50)
banana = Fruit("Banana", 0.75)
orange = Fruit("Orange", 1.20)

cart = ShoppingCart()

cart.add_item(apple, 3)
cart.add_item(banana, 5)
cart.add_item(orange, 2)
cart.add_item(apple, 2)

cart.display_cart()

cart.remove_item(banana, 2)
cart.display_cart()

cart.remove_item(orange) 
cart.display_cart()

cart.remove_item(Fruit("Grape", 3.00)) 
