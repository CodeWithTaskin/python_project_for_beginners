import random as r
randomGuess = r.randint(1,100)
print(randomGuess)
life = 5
life1 = 10


userChoice = input("Choose a difficulty. Type 'easy' or 'hard': ")
while True:
    if userChoice.lower() == "easy":
        user = int(input("Make a Guess: "))
        if user > randomGuess:
            life1 -= 1
            print("Too high...\nGuess again.")
            print(f"You have {life1} attempts remaining to guess the number.")
        elif user < randomGuess:
            life1 -= 1
            print("Too low...\nGuess again.")
            print(f"You have {life1} attempts remaining to guess the number.")
        elif user == randomGuess:
            print(f"You got it. The answer was {randomGuess}")
            break
    else:
        user = int(input("Make a Guess: "))
        if user > randomGuess:
            life -= 1
            print("Too high...\nGuess again.")
            print(f"You have {life} attempts remaining to guess the number.")
        elif user < randomGuess:
            life -= 1
            print("Too low...\nGuess again.")
            print(f"You have {life} attempts remaining to guess the number.")
        elif user == randomGuess:
            print(f"You got it. The answer was {randomGuess}")
            break
    if life1 == 0 or life == 0:
        print("You lost!!!!")  
        break 
        