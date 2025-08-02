# Menu items and their prices
menu = {
    'Burger': 5.99,
    'Pizza': 8.99,
    'Salad': 4.50,
    'Soda': 1.99,
    'Fries': 2.99
}

# List of customers and their orders (how many of each item they bought)
customers = {
    'Alice': {'Burger': 2, 'Soda': 2},
    'Bob': {'Pizza': 1, 'Fries': 1, 'Soda': 1},
    'Charlie': {'Salad': 3, 'Soda': 1}
}

# Print the menu
print("Menu:")
for item, price in menu.items():
    print(f"  {item}: ${price:.2f}")

print("\nCustomer Orders and Totals:")

# Calculate and display total for each customer
for customer, orders in customers.items():
    print(f"\n{customer} bought:")
    total = 0
    for item, quantity in orders.items():
        if item in menu:
            item_total = menu[item] * quantity
            print(f"  {quantity} x {item} @ ${menu[item]:.2f} each = ${item_total:.2f}")
            total += item_total
    print(f"Total for {customer}: ${total:.2f}")