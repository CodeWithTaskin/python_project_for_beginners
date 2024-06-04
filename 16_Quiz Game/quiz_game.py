print("Hi, Welcome To My Quiz Game !!!!")

point = 0
ans = input("Do you want to answer? ")
if ans == "yes":
    print("Ok! Let's play\n")

Q1 = input("In which year did the Titanic sink? ")
if Q1 == "1912":
    print("Your Answer is currect. You have 1 point\n")
    point+=1
else:
    print("Your Answer is wrong!!")

Q2 = input("What is the chemical symbol for gold? ")
if Q2 == "Au":
    print("Your Answer is currect. You have 1 point\n")
    point+=1
else:
    print("Your Answer is wrong!!")

Q3 = input("Who is known as the 'Father of Computers'? ")
if Q3 == "Charles Babbage":
    print("Your Answer is currect. You have 1 point\n")
    point+=1
else:
    print("Your Answer is wrong!!")

Q4 = input("What is the capital of France? ")
if Q4 == "Paris":
    print("Your Answer is currect. You have 1 point\n")
    point+=1
else:
    print("Your Answer is wrong!!")

Q5 = input("What is the largest planet in our solar system? ")
if Q5 == "Jupiter":
    print("Your Answer is currect. You have 1 point\n")
    point+=1
else:
    print("Your Answer is wrong!!")

print(f"You have {point} out of 5")