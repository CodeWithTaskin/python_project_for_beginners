import random as r
from random_word import random_word as rw
from Hangmanpic import HANGMANPICS
print("""
 
                    _______
                  |/      |
                  |      (_)
                  |      \|/
                  |       |
                  |      / \\
                  |
 _               _|___                          
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ 

        """)


word = r.choice(rw)
life = 8
death = -1
hide_word = ["_" for i in range(len(word))]
print(hide_word)
while True:
  userInput = input("Guess word: ")
  if userInput in hide_word:
    print("Don't over write!!!")
  for i in range(len(word)):
    if userInput == word[i]:
      hide_word[i]=word[i]
  print(hide_word)
  if userInput not in word:  
    life -= 1
    death += 1
    print(f"Oop's worng guess!!! You have {life} life...")
    print(HANGMANPICS[death])
  if "_" not in hide_word:
    print("You are winner!!!")
    break
  elif life == 0:
    print("You lost your all life")
    break