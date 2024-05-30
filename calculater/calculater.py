while True:
    try:
     print("""
Welcome to my simple calculator
-------------------------------
            """)
     firstNum = int(input("Enter your first number: "))
     secundNum = int(input("Enter your secund number: "))
     
     def addition(a,b):
        return a+b
     def subtraction(a,b):
        return a-b
     def multiplication(a,b):
        return a*b
     def division(a,b):
        return a/b
     def divisionWithreminder(a,b):
        return a%b
     print("""
Choice your operation from the list:
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Division With Reminder          
""")
     choice = int(input("Enter your choice: "))
     if choice == 1:
        print(addition(firstNum,secundNum))
     elif choice == 2:
        print(subtraction(firstNum,secundNum))
     elif choice == 3:
        print(multiplication(firstNum,secundNum))
     elif choice == 4:
        print(division(firstNum,secundNum))
     elif choice == 5:
        print(divisionWithreminder(firstNum,secundNum))
     Exit = input("Do you want to exit?(Y?N): ")
     if Exit.lower() == "y":
        break
    except:
       print("Invalid Input")