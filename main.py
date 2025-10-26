"""
This is an interactive shopping program that lets users
by different types of clothes given a budget. It also helps
begginner programmers (like myself) understand how hidden
attributes, methods, and objects work together through
this real-world example.
"""

print("--- Welcome to the Virtual Closet! ---") # welcome message

class ClothingItem:
    def __init__(self, name, price, budget):
        self.name = name
        self.price = price
        self.__budget = budget # hidden attribute

    def get_budget(self):  # getter method
        return self.__budget

    def set_budget(self, new_budget): # setter method
        if new_budget >= 0:
            self.__budget = new_budget
        else:
            print("Budget can't be negative!")

    def __repr__(self):
        return self.name + " - $" + str(self.price) + " (Budget left: $" + str(self.__budget) + ")"

# 2D list of clothing categories and items
clothing_catalog = [
    ["Shirt", "T-Shirt", "Blouse"],
    ["Jeans", "Shorts", "Skirt"],
    ["Jacket", "Sweater", "Hoodie"]
]

# dictionary of inventory
inventory = {
    "Shirt": ClothingItem("Shirt", 25.00, 100),
    "T-Shirt": ClothingItem("T-Shirt", 20.00, 100),
    "Blouse": ClothingItem("Blouse", 30.00, 100),
    "Jeans": ClothingItem("Jeans", 40.00, 100),
    "Shorts": ClothingItem("Shorts", 22.00, 100),
    "Skirt": ClothingItem("Skirt", 28.00, 100),
    "Jacket": ClothingItem("Jacket", 50.00, 100),
    "Sweater": ClothingItem("Sweater", 35.00, 100),
    "Hoodie": ClothingItem("Hoodie", 38.00, 100)
}

def display_catalog():
    categories = ["Tops", "Bottoms", "Outerwear"]
    for i, category in enumerate(clothing_catalog):
        print()
        print(categories[i] + ":")
        for item in category:
            print("  - " + str(inventory[item]))

# function that handles checkout
def checkout(item_name, quantity):
    item = inventory.get(item_name)
    if not item:
        print("Item not found.")
        return

    current_budget = item.get_budget()
    total_price = quantity * item.price

    if total_price <= current_budget:
        purchase_info = (item.name, quantity, total_price)

        name, qty, cost = purchase_info

        print()
        print("You are buying " + str(qty) + " " + name + "(s) for $" + str(cost) + ".")

        item.set_budget(current_budget - cost)  # using setter method
        
        new_item = ClothingItem(name, item.price, item.get_budget())
        print("Are the item names equal? " + str(item.name == new_item.name))

        print("Are these the same object? " + str(item is new_item))

    else:
        print("Not enough budget to buy " + item.name + ". You need $" + str(total_price) + ", but only have $" + str(current_budget) + ".")

# taking user input
name = input("Enter your name: ")
print("Hello, " + name + "! Let's go shopping!")

while True:
    display_catalog()

    print()
    item_name = input("What item would you like to buy? (Capitalize item name): ")
    if item_name not in inventory:
        print("Sorry, that item doesn't exist. Try again.")
        continue

    try:
        quantity = int(input("How many " + item_name + "(s) would you like to buy?: "))
        if quantity <= 0:
            print("Quantity must be positive.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    checkout(item_name, quantity)

    print()
    again = input("Would you like to buy something else? (yes/no): ")
    if again.lower() != "yes":
        print("Thanks for shopping, " + name + "!")
        break
