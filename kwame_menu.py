# Define the menu as a dictionary
def getListOnMenu():
    return {
        "Goat Jollof": 50,
        "Fried Rice": 45,
        "Banku and Tilapia": 70,
        "Waakye": 60
    }

# Function to take an order and calculate totals
def take_order():
    menu = getListOnMenu()
    print("This is our menu for today:")
    for item, price in menu.items():
        print(f"{item}: ${price}")

    order = {}
    while True:
        item = input("Please select an item from our menu (or type 'done' to finish): ")
        if item.lower() == 'done':
            break
        if item not in menu:
            print("Sorry, that item is not on the menu. Please choose again.")
            continue
        quantity = input(f"How many {item} would you like to order? ")
        if not quantity.isdigit() or int(quantity) <= 0:
            print("Please enter a valid positive number for quantity.")
            continue
        quantity = int(quantity)
        if item in order:
            order[item] += quantity
        else:
            order[item] = quantity

    total_price = sum(menu[item] * qty for item, qty in order.items())
    total_quantity = sum(order.values())
    return order, total_price, total_quantity

# Main program
print("Welcome to Pause N Chop restaurant:\n")
CustomersDay = input("How has your day been? ")
print("Lovely, good to hear that")

customerName = input("What is your name?\n")
print("You are welcome, " + customerName + " to our lovely restaurant once again.")

order, total_price, total_quantity = take_order()

print(f"\nThank you, {customerName}, for your order.")
print(f"You ordered: {order}")
print(f"Total quantity: {total_quantity}")
print(f"Total price: ${total_price}")