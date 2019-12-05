#import sys #this allows you to use the sys.exit command to quit/logout of the application
from array import *
import os

print("Welcome to MF.JFAM's Dungeon Run!")
def print_map(grid, map_Size):
    for i in range(map_Size):
        for j in range(map_Size):
            print(grid[i,j], end=" ")
        print() 


def int_input(question):
    while True:
        try:
            user_input = int(input(question))
            if user_input < 4 and user_input > 0:
                return user_input
            else:
                os.system("cls")
                print("You make your choice by entering 1,2 or 3.")
        except ValueError:
            os.system("cls")
            print("You make your choice by entering 1,2 or 3.")
            int_input(question)
def accepted_Hero_Input(question):
    answer = str(input(question))
    answer = answer.lower()
    if answer == "y" or answer == "n":
        return answer
    else:
        print("Please enter y for yes or n for no.")
        accepted_Hero_Input(question)
def create_map(map_Size):
    grid_map = {}
    for x in range(map_Size):
        for y in range(map_Size):
            grid_map[(x,y)] = "x"
    return grid_map

def main():
    login()
    
def login():
    print("***********************************")
    print("*          Game Main Menu         *")
    print("***********************************")
    print()
main()
correct = True
while correct:
    name = input("Please Input Your User Name: ")
    if name == "mfjap". lower():
        pw = input("Please Enter Your Password:")
        if pw == "agile":
            print("Welcome To The Game Zone:")
            break
        if pw != "agile":
            pwi = input("Passwoed Incorrect")
            if pwi == "y".lower():
                correct = True
            else:
                print("Thank You For Trying Login, Goodbye")
                quit()
    if name != "MFJAP".lower():
        uni = input("User Name Is Not Valid, Will You Try Agin Y/N?")
        if uni == "y".lower():
            correct == True
        else:
            print("Good Try")
            quit()

while True:
    os.system("cls")
    hero_Choice = int_input("What hero do you wanna play?\n1.Knight\n2.Wizard\n3.Thief\n> ")
    print("\n")
    if hero_Choice == 1:
        print("--Knight--\nInitiative 5\nDurability 9\nAttack 6\nFlexibility 4\n"
        "\nThe knight's special ability is Shieldblock. Avoid damage on the first attack")
        answer = accepted_Hero_Input("Do you wanna play with the Knight? y/n \n>")
        hero = "Knight"
    if hero_Choice == 2:
        print("--Wizard--\nInitiative 6\nDurability 4\nAttack 9\nFlexibility 5\n"
        "\nThe wizard's special ability is Flash of Light. An 80% chance to escape from combat")
        answer = accepted_Hero_Input("Do you wanna play with the Wizard? y/n \n>")
        hero = "Wizard"
    if hero_Choice == 3:
        print("--Thief--\nInitiative 7\nDurability 5\nAttack 5 \nFlexability 7\n"
        "\nSpecial Ability: Critical Hit. The thief has 25% chance to do double damage with each attack.")
        answer = accepted_Hero_Input("Do you wanna play with the Thief? y/n \n>")
        hero = "Thief"
    if answer == "y":
        break
os.system("cls")
print(f"Playing as {hero}!")
map_Choice = int_input("What map size do you wanna play?\n1.Small\n2.Medium\n3.Large\n> ")

if map_Choice == 1:
    map_Size = 4
if map_Choice == 2:
    map_Size = 5
if map_Choice == 3:
    map_Size = 8

grid_map = create_map(map_Size)
os.system("cls")
while True:
    right_input = ("1","2","3","4")
    start_pos_input = str(input("What corner you wanna start in?\n1.Up left\n2.Up right\n3.Down left\n4.Down right\n> "))
    if start_pos_input in right_input:
        if start_pos_input == "1":
            start_pos_x = 0
            start_pos_y = 0
        if start_pos_input == "2":
            start_pos_x = 0
            start_pos_y = map_Size - 1
        if start_pos_input == "3":
            start_pos_x = map_Size - 1
            start_pos_y = 0
        if start_pos_input == "4":
            start_pos_x = map_Size - 1
            start_pos_y = map_Size - 1
        os.system("cls")
        break
    else:
        os.system("cls")
        print("You make your choice by entering 1, 2, 3 or 4")
grid_map[start_pos_x,start_pos_y] = "@"
hero_pos = [start_pos_x, start_pos_y]
while True:
    os.system("cls")
    print_map(grid_map,map_Size)
    grid_map[hero_pos[0], hero_pos[1]] = "o"
    movement = str(input("Where do you wanna go? Use W for up, A for left, D for right, S for down."))
    if movement == "w":
        hero_pos[0] = hero_pos[0] - 1
    if movement == "s":
        hero_pos[0] = hero_pos[0] + 1
    if movement == "d":
        hero_pos[1] = hero_pos[1] + 1
    if movement == "a":
        hero_pos[1] = hero_pos[1] - 1

    if movement == "q":
        break
    #If the hero walk too far down.
    if hero_pos[0] > map_Size - 1:
       print("You cant go that way!")
       hero_pos[0] = hero_pos[0] - 1
    #If the hero walk too far up.
    if hero_pos[0] < 0:
        print("You cant go that way!")
        hero_pos[0] = hero_pos[0] + 1
    #If the hero walk too far right.
    if hero_pos[1] > map_Size - 1:
        print("You cant go that way!")
        hero_pos[1] = hero_pos[1] - 1
    #If the hero walk too far left.
    if hero_pos[1] < 0:
        print("You cant go that way!")
        hero_pos[1] = hero_pos[1] + 1
    else:
        grid_map[hero_pos[0], hero_pos[1]] = "@"
    main()
    #sys.exit()
