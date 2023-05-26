import csv
print("This is Pizza Shop---------------------------------------------------------")

# cart for user
user_cart = {}

#pizza list start
pizzaList = {
    "cheese": {"name" : "Cheese Pizza", 'price':300},
    "veggie" :{"name" : "Veggie Pizza", 'price':250},
    "pepperoni": {"name" : "Pepperoni Pizza", "price":300},
    "meat" :{"name" : "Meat Pizza", "price":400},
} 

#topping Menu
toppinglist = {
    "sausage": {"name" : "Sausage", "price":200},
    "mushroom": {"name" : "Mushroom", "price":250},
    "tomato": {"name" : "Tomato", "price":300},
    "onions": {"name" : "Onions", "price":200},
}

def showPizza():
    print("The Pizza list are: ")
    for i in pizzaList.values():
        print(f"{i['name']} Rs: {i['price']}")


def showTopping():
    print("The Topping list are : ")
    for t_menu in toppinglist.values():
        print(f"{t_menu['name']} Rs: {t_menu['price']}")

#buying code start here 
def buy(user= None):
    print("select Pizza --------------------------------------------------------------------:")
    showPizza()
    selected_pizza = input("Enter Name for select pizza : ")
    pizza = pizzaList.get(selected_pizza)
    if pizza:
        print(f" You Select {pizza['name']} With Price Rs: {pizza['price']}")
    else:
        print("Selected Pizza is not in list")
        
    

    print("select Topping --------------------------------------------------------------------:")
    showTopping()
    selected_topping = input("Enter Name for select Topping : ")
    topping = toppinglist.get(selected_topping)
    if topping:
        
       print(f"You select {topping['name']} with price Rs: {topping['price']} ")
    else:
        print("Selected topping not in list")

    quantity = int(input("Enter Quantity :"))
    pizza_Topping_Price = pizza['price'] + topping['price']
    total_price = pizza_Topping_Price * quantity
    print(f"You Purchase {pizza['name']} with tipping {topping['name']} Rs: {pizza_Topping_Price} with quantity {quantity} is : {total_price}")

    # user_cart['user', 'pizza', 'topping', 'total'] = user, selected_pizza, selected_topping, total_price
    user_cart['user'] = user
    user_cart['pizza'] = selected_pizza
    user_cart['topping'] = selected_topping
    user_cart['total'] = total_price

    with open('cart.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            with open('cart.csv', 'r') as file_read:
                reader = csv.reader(file_read)
                row_count = sum(1 for row in reader)
        
                row = [row_count - 1] + list(user_cart.values())
        
                writer.writerow(row)

# user input starts here
auth_user = False
def auth(user = None):
    if user == None:
        user = input("Enter User :")
        with open('user.txt', 'r') as f:
            data = f.read()
            for i in data:
                if user in data:
                    auth_user = True
                else:
                    print("OPPS! User is not none Try again with Registered user")
                    auth_user = False
                    auth()
    else:
        auth_user = True
    if auth_user:
        print("You are registered user")
        select_user = int(input("""Enter '1' for See pizza list :
        '2' for See Topping List: ,
        '3' for See Buy :
        """))

        
    
        if select_user == 1:
            showPizza()
            repeat = input("Enter y for Continue:")
            if repeat == 'y':
                auth(user)

        elif select_user == 2:
            showTopping()
            repeat = input("Enter y for Continue: ")
            if repeat == 'y':
                auth(user)

        elif select_user == 3:
            buy(user)
            for i in user_cart.items():
                print(i)
            repeat = input("Enter y for Buy anohter: ")
            if repeat == 'y':
                buy(user)


auth()






