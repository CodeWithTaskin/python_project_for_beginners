import random as r

symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
lowercase_letters = [chr(i) for i in range(97, 123)]  # 'a' to 'z'
uppercase_letters = [chr(i) for i in range(65, 91)]   # 'A' to 'Z'
number = [str(i) for i in range(0, 10)]             # '0' to '9'
passlist = []
userName = input("Account Name: ")
def passdet(a,b,c,d):
    a = input(f"Do you want {a} Y/N : ")
    if a == "Y":
        b = int(input(f"How many {d} you want? ==> "))
        for i in range(b+1):
            passlist.append(r.choice(c))

            
passdet("lowercase","userWantLower",lowercase_letters,"lowercase")
passdet("uppercase","userWantUpper",uppercase_letters,"uppercase")
passdet("numbers","userWantNumbers",number,"numbers")
passdet("symbols","userWantSymbels",symbol,"symbols")

newPassList = []
for a in range(len(passlist)):
    newPassList.append(r.choice(passlist))

password = ''.join(newPassList)
print(f"\n\n\nAccount Name: {userName}\nPassword: {password}\nLenth of Password: {len(password)}\n\n")

# --------------------------- Save Password --------------------------------

passwordFileName = input("""Enter file path that you want 'NOTE: If you don't enter file path set name then it set defult path': """)
with open(f"{passwordFileName}","a") as passwordfile:
    passwordfile.write(f"""Name: {userName}\nPassword: {password}\nLenth of Password: {len(password)}""")

print("\n\n\nThank you")
input("\nIf you want to close this program enter 'Y'")

# userChoiceLower = input("Do you want lowercase letter? Y/N : ")
# if userChoiceLower == "Y":
#     userWantLower = int(input("How many lowercase letter you want? ==> "))
#     for i in range(userWantLower):
#         passlist.append(r.choice(lowercase_letters))
    
# userChoiceUpper = input("Do you want uppercase letter? Y/N : ")
# if userChoiceUpper == "Y":
#     userWantUpper = int(input("How many uppercase letter you want? ==> "))
#     for i in range(userWantUpper):
#         passlist.append(r.choice(uppercase_letters))

# userChoiceNumber = input("Do you want numbers? Y/N : ")
# if userChoiceNumber == "Y":
#     userWantNumber = int(input("How many numbers you want? ==> "))
#     for i in range(userWantNumber):
#         passlist.append(r.choice(numbers))

# userChoiceSymbols = input("Do you want symbols? Y/N : ")
# if userChoiceSymbols == "Y":
#     userWantSymbols = int(input("How many symbols you want? ==> "))
#     for i in range(userWantSymbols):
#         passlist.append(r.choice(symbols))



