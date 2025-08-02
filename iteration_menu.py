#pause_chop menu

#define menu
def getListOnMenu ():
    ListOnMenu = {
        "Goat Jollof": 50, 
        "Fried Rice": 45, 
        "Banku and Tilapia":70, 
        "Waakye":60
        }
    return ListOnMenu

def take_order():
    menu = getListOnMenu()
    print("This is our menu for today:")
    for item, price in menu.items():
        print(f"{item}: ${price}")
 
def itemX_price (itemX):
    itemXPrice = 0
    menu = getListOnMenu()
    for key, value in menu.items():
        if itemX in key:
            itemXPrice = value
            break 
   
    return itemXPrice

#Welcome the customer
print("Welcome to Pause N Chop restaurant:\n")
#Ask how they are feeling
CustomersDay= input("How has your day being?")
#Say something nice
print("Lovely, good to hear that")


#customers = getListOfCustomers()
#totalSalesForTheDay = 0

#def NameOfCustomer():
   # NameOfCustomer = getListOfCustomers

#order = {}
#Get customers name
customerName = input("What is your name?\n")


print("You are welcome, " + customerName +  " to our lovely restaurant once again.")


#print(take_order())

#getListOfCustomers ()


itemX= input("Please select from our menu.\n")

print("Excellent choice!!!")

quantity= input("How many item would you like to order?")

quantity= int(quantity)

itemXPrice = itemX_price (itemX)

totalPrice = quantity * itemXPrice

print(f"Confirm that the total amount is {totalPrice}")