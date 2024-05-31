counter = 0
with open("count.txt","r") as count:
    while 1:
        char = count.read(1)          
        if not char: 
            break
        if char == " ":
            counter += 1

print(f"{counter+1} word in this text")

