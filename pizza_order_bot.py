# Mohamad Hussam Refaai

# Defining menu variables
pizza_menu = ["Veggie - $1.99", "Meat - $1.99", "Hawaiian - $1.99", "Cheese - $1.99"]
pizza_list = ["veggie", "meat", "hawaiian", "cheese"]
drink_menu = ["Water - Free", "Coke Zero - $0.75", "Cranberry - $0.75", "Fanta - $0.75", "Sprite - $0.75"]
drink_list = ["water", "coke zero", "cranberry", "fanta", "sprite"]
pizza_price = 1.99
drink_price = 0.75

# Greetings
print("Hello! Welcome to the ASB Pizza Party! Here is our menu:\n")

# Displaying the drinks menu
print("  DRINKS")
for drink in drink_menu:
    print("  -", drink)

# Displaying the pizza menu
print("\n  PIZZA")
for pizza in pizza_menu:
    print("  -", pizza)

# Asking user for a drink
ask_drink = input("\nWould you like a drink (yes/no)? ").lower().strip('!. ')
order_price_drinks = 0  # Initialize drink order price

if ask_drink == 'yes':
    what_type = input("What drink would you like? ").lower().strip('!. ')
    if what_type in drink_list:
        quantity = int(input("Sounds good. How many? ").strip('!. '))
        print(f"Got it, {quantity} {what_type}(s).")
        if what_type == "water":
            order_price_drinks = 0
        else:
            order_price_drinks = drink_price * quantity
    else:
        print("Sorry, we don't have that.")
else:
    print("Alright, got it!")

# Asking user for pizza
ask_pizza = input("\nAnd what pizza would you like? ").lower().strip('!. ')
order_price_pizza = 0  # Initialize pizza order price

if ask_pizza in pizza_list:
    quantity_1 = int(input("Ok! How many of those? ").strip('!. '))
    order_price_pizza = pizza_price * quantity_1
    print(f"Got it, {quantity_1} {ask_pizza}(s).")
else:
    print("Sorry, we don't have that.")

# Calculating the total price with tax
total_cost = order_price_pizza + order_price_drinks
total_cost_tax = total_cost * 1.05  # Applying 5% tax

# Displaying the total price
print(f"\nYour total with tax will be ${total_cost_tax:.2f}. Enjoy!")
