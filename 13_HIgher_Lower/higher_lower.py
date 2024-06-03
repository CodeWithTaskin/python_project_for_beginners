from game_data import data
from replit import clear
import random as r
import art

print(art.logo)
all_data = []
follower_count = []
point = 0
for i in data:
    all_data.append(i["name"]+" "+i["description"]+" "+i["country"])
for j in data:
    follower_count.append(j["follower_count"])
while True:
    candidate1 = r.randrange(len(all_data)+1)
    candidate2 = r.randrange(len(all_data)+1)
    print(f"Compare A : {all_data[candidate1]}.")
    print(art.vs)
    print(f"Compare B : {all_data[candidate2]}.")
    ans = input("Who has more followers? A or B : ")
    if ans.lower() == "a":
        a = candidate1
        if follower_count[a] > follower_count[candidate2]:
            print(follower_count[a])
            print(follower_count[candidate2])
            point+=1
            clear()
        else:
            print(follower_count[a])
            print(follower_count[candidate2])
            print(f"Sorry, Final answer is {point}")
            break
    elif ans.lower() == "b":
        b = candidate2
        if follower_count[b] > follower_count[candidate1]:
            print(follower_count[candidate1])
            print(follower_count[b])
            point+=1
            clear()
        else:
            print(follower_count[candidate1])
            print(follower_count[b])
            print(f"Sorry, Final answer is {point}")
            break
    




