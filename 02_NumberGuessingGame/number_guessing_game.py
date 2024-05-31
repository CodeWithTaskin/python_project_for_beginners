import random as r
randomGuess = r.randint(1,20)
print(randomGuess)
while True:
    try:
        userGuess = int(input("Enter a number between 1-20: "))
        if userGuess > randomGuess:
            print("wrong! Too Higher....")
        elif userGuess < randomGuess:
            print("Wront! Too Lower....")
        else:
            print(f"""That's right randon guess is ==> {randomGuess} <== and Your guess is ==> {userGuess} <==!!!""")
            break
    except:
        print("Invalid Input")