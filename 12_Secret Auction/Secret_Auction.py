from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
dic = dict()
name = input("What is your name? ")
bid_amount = int(input("What is your bid $"))
dic[name]= bid_amount
while True:
    userChoice = input("Do you want to bid(Y/n)? ")
    if userChoice.lower() == "y":
        clear()
        name = input("What is your name? ")
        bid_amount = int(input("What is your bid $"))
        dic[name]= bid_amount
    else:
        clear()
        key_list = list(dic.keys())
        value_list = list(dic.values())
        position = value_list.index(max(value_list))
        print(f"The winner is {key_list[position]} bid ${max(value_list)}")
        break