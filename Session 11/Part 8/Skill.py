import random
from random import randint
Character = {
    "Name": "Light",
    "Age": 17,
    "Strength": 8,
    "Defense": 10,
    "HP": 100,
    "Backpack": ["Shield", "Bread Loaf"],
    "Gold": 100,
    "Level": 35,
}
skill_1 = {
    "Name": "Tackle",
    "Minimum Level": 10,
    "Damage": 5,
    "Hit Rate": 0.3,
}
skill_2 = {
    "Name": "Quick Attack",
    "Minimum Level": 20,
    "Damage": 3,
    "Hit Rate": 0.5,
}
skill_3 = {
    "Name": "Strong Kick",
    "Minimum Level": 40,
    "Damage": 9,
    "Hit Rate": 0.2,
}
Skills = []
Skills.append(skill_1)
Skills.append(skill_2)
Skills.append(skill_3)

# for i in range (3):
#     print(i+1, Skills[i]["Name"])

print("Match started")
print("You are: ", Character["Name"])
print("Your level is: ", Character["Level"])
print("Available skills: ")
for i in range(3):
    print(i+1,":",Skills[i]["Name"])
while True:
    n = input("Choose skills 1,2, or 3: ")
    if n.isnumeric():
        n = int(n)
        print("You have chosen skill: ", Skills[n-1]["Name"])
        if Character["Level"] >= Skills[n-1]["Minimum Level"]:
            print("Skill Usable")
            d = input("Engage? ")
            if d == "yes":
                rate = random.randint(0,1)
                if rate < Skills[n-1]["Hit Rate"]:
                    print("Damage Impact: ", Skills[n-1]["Damage"])
                    choice = input("Quit game? ")
                    if choice == "yes": break
                else: 
                    print("Missed")
                    choice = input("Quit game? ")
                    if choice == "yes": break
            elif d == "no":
                print("Engage Cancelled")
                choice = input("Quit game? ")
                if choice == "yes": break
            else:  
                print("Please Choose Again")
                choice = input("Quit game? ")
                if choice == "yes": break
        else: 
            print("Not Enough Level")
            choice = input("Quit game? ")
            if choice == "yes": break
    else: 
        print("Invalid Skill")
        choice = input("Quit game? ")
        if choice == "yes": break