from data import MENU
from art import logo

water = 300
milk = 200
coffee = 100
money = 0


def cost(quaters,dimes,nickles,pennice):
    pen = 0.01*pennice
    nickl = 0.05*nickles
    dim = 0.10*dimes
    quat = 0.25*quaters
    return pen+nickl+dim+quat
def espresso():
    coffee_water = MENU["espresso"]["ingredients"]["water"]
    coffee_for_espresso = MENU["espresso"]["ingredients"]["coffee"]
    cost_for_coffee = MENU["espresso"]["cost"]
    return cost_for_coffee,coffee_water,coffee_for_espresso
def latte():
    coffee_water = MENU["latte"]["ingredients"]["water"]
    coffee_for_latte = MENU["latte"]["ingredients"]["coffee"]
    milk_for_latte = MENU["latte"]["ingredients"]["milk"]
    cost_for_coffee = MENU["latte"]["cost"]
    return cost_for_coffee,coffee_water,coffee_for_latte,milk_for_latte
def cappuccino():
    coffee_water = MENU["cappuccino"]["ingredients"]["water"]
    coffee_for_cappuccino = MENU["cappuccino"]["ingredients"]["coffee"]
    milk_for_cappuccino = MENU["cappuccino"]["ingredients"]["milk"]
    cost_for_coffee = MENU["cappuccino"]["cost"]
    return cost_for_coffee,coffee_water,coffee_for_cappuccino,milk_for_cappuccino
def coins():
    quaters = int(input("How many quaters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennice = int(input("How many pennice? "))
    return quaters,dimes,nickles,pennice



print(logo)
while True:
    try:
        userChoice = input("What would you like? (espresso/latte/cappuccino): ")
        if userChoice.lower() == "espresso":
            print("Please insert coins.")
            quaters,dimes,nickles,pennice = coins()
            cost_for_coffee,coffee_water,coffee_for_espresso = espresso()
            userMoney = cost(quaters,dimes,nickles,pennice)
            if userMoney >= cost_for_coffee:
                if coffee_water <= water and coffee_for_espresso <= coffee :
                    change = userMoney - cost_for_coffee
                    money += cost_for_coffee
                    water -= coffee_water
                    coffee -= coffee_for_espresso
                    if change == 0:
                        print("Here is your espresso ☕️. Enjoy!")
                        pass
                    else:
                        print(f"Here is ${change} in change.")
                        print("Here is your espresso ☕️. Enjoy!")
                else:
                    print("Sorry we are runout!!!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        elif userChoice.lower() == "latte":
            print("Please insert coins.")
            quaters,dimes,nickles,pennice = coins()
            cost_for_coffee,coffee_water,coffee_for_latte,milk_for_latte = latte()
            userMoney = cost(quaters,dimes,nickles,pennice)
            if userMoney >= cost_for_coffee:
                if coffee_water <= water and coffee_for_latte <= coffee :
                    change = userMoney - cost_for_coffee
                    money += cost_for_coffee
                    water -= coffee_water
                    coffee -= coffee_for_latte
                    milk -= milk_for_latte
                    if change == 0:
                        print("Here is your latte ☕️. Enjoy!")
                        pass
                    else:
                        print(f"Here is ${change} in change.")
                        print("Here is your latte ☕️. Enjoy!")
                else:
                    print("Sorry we are runout!!!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        elif userChoice.lower() == "cappuccino":
            print("Please insert coins.")
            quaters,dimes,nickles,pennice = coins()
            cost_for_coffee,coffee_water,coffee_for_cappuccino,milk_for_cappuccino = cappuccino()
            userMoney = cost(quaters,dimes,nickles,pennice)
            if userMoney >= cost_for_coffee:
                if coffee_water <= water and coffee_for_cappuccino <= coffee :
                    change = userMoney - cost_for_coffee
                    money += cost_for_coffee
                    water -= coffee_water
                    coffee -= coffee_for_cappuccino
                    milk -= milk_for_cappuccino
                    if change == 0:
                        print("Here is your cappuccino ☕️. Enjoy!")
                        pass
                    else:
                        print(f"Here is ${change} in change.")
                        print("Here is your cappuccino ☕️. Enjoy!")
                else:
                    print("Sorry we are runout!!!")
            else:
                print("Sorry that's not enough money. Money refunded.")
            
        elif userChoice.lower() == "report":
            print(f"Wather: {water}")
            print(f"Milk: {milk}")
            print(f"Coffee: {coffee}")
            print(f"Money: ${money}")
        elif userChoice.lower() == "off":
            break
    except:
        print("Invalid Input!!!")
