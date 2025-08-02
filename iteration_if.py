print("I am sacking school feeeeeeeeeeeeeees!!!!" )

name = input("what is your name?\n")

if name == "speedo":
    print("go home, you poor boy!!!")
    print("wo canteen sika no, ahye")

else:
    print("Hello " + name +", you do not owe school fees. Go sit down!")
    print("Your father is very responsible.")
    print("Wob3di canteen no bi.")


    for customers_name, orders in customers.items():
    print(f"{customers_name} : bought:")
    total = 0

    for item, quantity in orders.items():
        if item in menu_prices:
            item_total = menu_prices[item] * quantity
            print (f"{quantity} x {item} for {menu_prices[item]} each = {item_total}") 
            total += item_total
        else:
            print(f"{item} (price not found)")
    print(f"Total for {customers_name} : {total}")
    totalSalesForTheDay += total

    print(f"Today's Sales :{totalSalesForTheDay}")



