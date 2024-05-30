userInput = input("Enter a string to check: ")

def textTopalindrome(userInput):
    pal = []
    for i in range(1,len(userInput)+1):
        pal.append(userInput[-i])
        palindrome = "".join(pal)
    return palindrome
if textTopalindrome(userInput) != userInput:
    print("This text is not palindrome")
else:
    print("This text is palindrome")

