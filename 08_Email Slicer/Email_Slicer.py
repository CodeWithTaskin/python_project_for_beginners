user_email = input("Enter your email: ")
name = []
email = []
start = -1
for i,char in enumerate(user_email):
    if char != "@":
        name.append(user_email[i])
    if char == "@":
        start = i+1
        break

for i, char in enumerate(user_email[start:]):
    email.append(char)

print("Your name is ==>","".join(name),"<== and Domin is ==>","".join(email),"<==....")

