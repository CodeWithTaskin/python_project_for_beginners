import random as r

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
randomGuess = r.randint(0,2)
game = [rock, paper, scissors]
userGuess = int(input("Enter rock(0) or paper(1) or scissors(2): "))
if userGuess == randomGuess:
    print(game[userGuess])
    print(game[randomGuess])
    print("Drow Match!")
elif userGuess == 0 and randomGuess == 1:
    print(f"User {game[userGuess]}")
    print(f"Computer {game[randomGuess]}")
    print("User win!")
elif userGuess == 0 and randomGuess == 2:
    print(f"User {game[userGuess]}")
    print(f"Computer {game[randomGuess]}")
    print("Compuater win!")
elif userGuess == 1 and randomGuess == 0:
    print(f"User {game[userGuess]}")
    print(f"Computer {game[randomGuess]}")
    print("User win!")   
elif userGuess == 1 and randomGuess == 2:
    print(f"User {game[userGuess]}")
    print(f"Computer {game[randomGuess]}")
    print("Compuater win!")  
elif userGuess == 2 and randomGuess == 0:
    print(f"User {game[userGuess]}")
    print(f"Computer {game[randomGuess]}")
    print("Compuater win!")
elif userGuess == 2 and randomGuess == 1:
    print(f"User {game[userGuess]}")
    print(f"Computer {game[randomGuess]}")
    print("User win!")
    
