import os
import random
import time
import sys
import monster_superclass as msc
import hero_class as hc
import Treasures as t

def game_meny(inpt):
    """
        Prints out a pretty meny with a input.
    """
    print("*********************************************************")
    print(f"           {inpt}                                       ")
    print("*********************************************************")
def print_Slow(inpt):
    """
        Prints the input slow!
    """
    for char in inpt:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print("")
def print_map(grid, map_Size):
    """
        Prints out the map with two loops.
        Arguments are the grid(dict) and map size(int).
    """
    for x in range(map_Size):
        for y in range(map_Size):
            print(grid[x,y], end=" ")
        print() 
    print("\n")
def create_map(map_Size):
    """
        Creates the map with 2 for-loops. 
        It will be a dict where the keys are the x and y pos
        and the value will be x.
        Returns the Dict.
    """
    grid_map = {}
    for x in range(map_Size):
        for y in range(map_Size):
            grid_map[(x,y)] = "x"
    return grid_map

def int_input(question):
    """
        Error-handling for int questions. Argument is a text string.
        This only works for meny where you can only answer 1, 2 or 3.
        Returns the right answer.
    """
    while True:
        try:
            user_input = int(input(question))
            if user_input < 4 and user_input > 0:
                return user_input
            else:
                os.system("cls")
                print("You make your choice by entering 1, 2 or 3.")
        except ValueError:
            os.system("cls")
            print("You make your choice by entering 1, 2 or 3.")
def accepted_Hero_Input(question):
    """
        Error-handling for y or n. 
        Will return the answer.
    """
    answer = str(input(question))
    answer = answer.lower()
    if answer == "y" or answer == "n":
        return answer
    else:
        print("Please enter y for yes or n for no.")
        accepted_Hero_Input(question)

def chance_50():
    """
        Randomize a number between 1-100.
        Returns 1 or 0 depending on the random.
    """
    rad_int = random.randint(1,100)
    if rad_int >= 50:
        return 1
    else:
        return 0
def place_Treasure(grid_map):
    rooms = grid_map.keys()
    treasure_Room_Dict = {}
    for room in rooms:
        treasure_Room_Dict[room] = drop_Rate_Treasure()
        if treasure_Room_Dict[room] == None:
            del treasure_Room_Dict[room]
    return treasure_Room_Dict

def create_Treasure(treasures):
    treasures_List_Return = []
    treasure_Object = ""
    treasures_List = treasures.split(",")
    for treasure in treasures_List:
        if treasure == "Coins":
            treasure_Object = t.Treasure(2, "Coin")
        elif treasure == "Money Pouch":
            treasure_Object = t.Treasure(6, "Money Pouch")
        elif treasure == "Gold":
            treasure_Object = t.Treasure(10, "Gold")
        elif treasure == "Gemstone":
            treasure_Object = t.Treasure(14, "Gemstone")
        elif treasure == "Small Chest":
            treasure_Object = t.Treasure(20, "Small Chest")
        treasures_List_Return.append(treasure_Object)
    return treasures_List_Return
def drop_Rate_Treasure():
    return_Str = ""
    i = 0
    while i < 4:
        i += 1
        rnd_int = random.randint(1,100)
        if rnd_int <= 5:
            return_Str = return_Str + "Small Chest,"
            continue
        if rnd_int <= 10:
            return_Str = return_Str + "Gemstone,"
            continue
        if rnd_int <= 15:
            return_Str = return_Str + "Gold,"
            continue
        if rnd_int <= 20:
            return_Str = return_Str + "Money Pouch,"
            continue
        if rnd_int <= 40:
            return_Str = return_Str + "Coins,"
            continue
    if return_Str == "":
        return
    else:
        return return_Str.rstrip(",")
def place_Monster(grid_map):
    """
        Argument is the Map.
        Creates a monster room dict and the value will be 1 or 0.
        1 means there is a monster.
        Returns the monster room dict.
    """
    rooms = grid_map.keys()
    monster_room_dict = {}
    for room in rooms:
        i = chance_50()
        if i == 1:
            monster = spawn_Rate_Monster()
            monster_room_dict[room] = monster
    
    return monster_room_dict    
def dice_Roll(max_Rolls):
    """
        Argument max_Rolls, will roll a dice as many times as the value of max_Rolls.
        Returns the total of all the rolls 
    """
    i = 0
    dice_Total = 0
    while i < max_Rolls:
        rnd_int = random.randint(1,6)
        i = i + 1
        dice_Total += rnd_int
    return dice_Total
def spawn_Rate():
    """
        Will spawn a random monster,
        Returns a text string of the monster.
        Can spawn multiple monsters.
    """
    rnd_int = random.randint(1,50)
    if rnd_int <= 5:
        return "Spider,Skeleton,Orc,Troll"
    elif 6 <= rnd_int <= 15:
        return "Spider,Skeleton,Orc"
    elif 16 <= rnd_int <= 30:
        return "Spider,Skeleton"
    elif 20 < rnd_int:
        return "Spider"
def spawn_Rate_Monster():
    return_Str = ""
    i = 0
    while i < 3:
        i += 1
        rnd_int = random.randint(1,50)
        if rnd_int <= 5:
            return_Str = return_Str + "Troll,"       
            continue
        if rnd_int <= 10:
            return_Str = return_Str + "Orc,"
            continue
        if rnd_int <= 15:
            return_Str = return_Str + "Skeleton,"
            continue
        if rnd_int <= 20:
            return_Str = return_Str + "Spider,"
            continue
    return_Str = return_Str.rstrip(",")
    return return_Str
def create_Monster(monster_Type):
    """
        Argument monster type, as a string.
        Will return a monster object.
    """
    if monster_Type == "Spider":
        monster_Object = msc.Spider()
    if monster_Type == "Skeleton":
        monster_Object = msc.Skeleton()
    if monster_Type == "Orc":
        monster_Object = msc.Orc()
    if monster_Type == "Troll":
        monster_Object = msc.Troll()
    return monster_Object

def hero_Attack(hero_Object, monster_Object):
    """
        Argument is Hero object and Monster object.
        Will return 0, 1 or 2 if the Theif crits.
    """
    #Will compare hero dmg to monster block, if hero dmg is higher then the hero will hit.

    hero_Dmg = dice_Roll(hero_Object.attack)
    monster_Block = dice_Roll(monster_Object.flexibility)

    if hero_Dmg > monster_Block:
        #Theif special attack
        if isinstance(hero_Object, hc.Thief):
            rnd_int = random.randint(1,100)
            #25% chance to make a critical hit.
            if rnd_int < 25:
                print_Slow(f"You crit the {monster_Object.name} for 2 DMG!")
                print_Slow(f"{monster_Object.name} got {monster_Object.immunity - 2} health left!")
                if monster_Object.immunity - 2 == -1:
                    print_Slow(f"You overkilled the {monster_Object.name} by 1 DMG!")
                return 2
        print_Slow(f"You hit the {monster_Object.name} for 1 DMG!")
        print_Slow(f"{monster_Object.name} got {monster_Object.immunity - 1} health left!")
        return 1
    else:
        print("You missed!")
        print_Slow(f"{monster_Object.name} got {monster_Object.immunity} health left!")
        return 0 

def monster_Attack(monster_Object, hero_Object):
    """
        Argument is Monster object and Hero object.
        Will return 1 or 0.
    """
    #Will compare monster dmg to hero block, if monster is higher then it hits.

    monster_Dmg = dice_Roll(monster_Object.attack)
    hero_Block = dice_Roll(hero_Object.flexibility)

    if monster_Dmg > hero_Block:
        print_Slow(f"The {monster_Object.name} hit you for 1 DMG!")
        print_Slow(f"You got {hero_Object.immunity - 1} health left!")
        return 1
    else:
        print_Slow(f"The {monster_Object.name} missed!")
        print_Slow(f"You got {hero_Object.immunity} health left!")
        return 0 

def start_Battle(start_Type, hero_Object, monster_Object):
    round_Counter = 0
    if start_Type == "Hero":
        print("Hero starts!\n")
        while True:
            round_Counter = round_Counter + 1
            x = input("Press Enter to hit!")
            os.system("cls")
            game_meny(f"Fighting a {monster_Object.name}")
            print("\n--Your Turn--\n")
            #Hero dmg will be either 0, 1 or 2 if the Thief crit.

            hero_Dmg = hero_Attack(hero_Object,monster_Object)
            monster_Object.immunity = monster_Object.immunity - hero_Dmg
            
            #If the monster dies
            if monster_Object.immunity <= 0:
                print(f"\nYou killed the {monster_Object.name}!")
                return "Monster"
            
            #Else it will hit
            else:
                print(f"\n--{monster_Object.name}s Turn--\n")
                
                #Special attack Knight
                if isinstance(hero_Object, hc.Knight) and round_Counter == 1:
                    print_Slow(f"You blocked the first attack from the {monster_Object.name}!")
                    continue
                
                #Monster dmg will either be 0 or 1
                monster_Dmg = monster_Attack(monster_Object, hero_Object)
                hero_Object.immunity = hero_Object.immunity - monster_Dmg
            
            #If hero dies    
            if hero_Object.immunity == 0:
                print("YOU DIED!")
                return "Hero"
            print("\n")
    #Same as above but here the starter will be monster
    else:
        os.system("cls")
        starter = f"{monster_Object.name} starts"
        while True:
            round_Counter = round_Counter + 1
            game_meny(f"Fighting a {monster_Object.name}")
            print(starter)
            print(f"--{monster_Object.name}s Turn--\n")

            #Special attack Knight
            if isinstance(hero_Object, hc.Knight) and round_Counter == 1:
                print_Slow(f"You blocked the first attack from the {monster_Object.name}!")
            else:
                #Monster dmg will either be 0 or 1
                monster_Dmg = monster_Attack(monster_Object, hero_Object)
                hero_Object.immunity = hero_Object.immunity - monster_Dmg
            
            if hero_Object.immunity == 0:
                print_Slow("YOU DIED!")
                return "Hero"

            else:
                print("\n--Your Turn--\n")
                hero_Dmg = hero_Attack(hero_Object,monster_Object)
                monster_Object.immunity = monster_Object.immunity - hero_Dmg

            if monster_Object.immunity <= 0:
                print(f"\nYou killed the {monster_Object.name}!")
                return "Monster"
            enter = input("\nPress enter to Continue")
            starter = ""
            os.system("cls")
def flee(flexibility):
    """
        Argument is Heros Flexibility,
        Will return 1 if you fleed else 0
    """
    chance_Flee = flexibility * 10
    rnd_int = random.randint(1,100)
    if chance_Flee > rnd_int:
        print("You succeeded to flee!")
        return 1
    else:
        return 0
def chance_10():
    rnd_int = random.randint(1,100)
    if rnd_int <= 10:
        return 1
    else:
        return 0
def exit_Map(grid_Map):
    rooms = grid_Map.keys()
    exit_Room = {}
    for room in rooms:
        i = chance_10()
        if i == 1:
            exit_Room[room] = ""
    if len(exit_Room) == 0:
        x = random.randint(0, map_Size)
        y = random.randint(0, map_Size)
        exit_Room[x,y] = ""
    return exit_Room

#Läsa in hela filen i lista, ta bort rätt elemnt, lägg till i lista, spara över nya lista till fil
def save_Game():
    global hero_Points
    temp_Save_List = []
    with open (path_Name, "r") as file:
        for line in file:
            temp_Save_List.append(line.rstrip("\n"))
        file.close
    search_Str = username + "," + hero
    for line in temp_Save_List:
        if search_Str in line:
            temp_Save_List.remove(line)
            save_Str = f"{username},{hero},{hero_Points}"
            temp_Save_List.append(save_Str)

    with open(path_Name,"w") as f:
        for line in temp_Save_List:
            print(line)
            f.write(line + "\n")
def load_Game(username_inpt):
    try:
        with open (path_Name,"r+") as f:
            user_Info = ""
            found_Username = 0
            data = f.readlines()
            for lines in data:
                username, hero, hero_Points = lines.split(",")
                if username_inpt == username:
                    found_Username = 1
                    hero_Points = hero_Points.rstrip("\n")
                    user_Info = f"Your {hero} has {hero_Points} points.\n" + user_Info
                    if hero == "Knight":
                        global knight_Points 
                        knight_Points = hero_Points
                    if hero == "Wizard":
                        global wizard_Points
                        wizard_Points = hero_Points
                    if hero == "Thief":
                        global thief_Points
                        thief_Points = hero_Points
            return user_Info, found_Username
    except FileNotFoundError:
        print("Filen finns inte")

game_meny("Welcome to MF.JFAM's Dungeon Run!")
#Userame will be linked to the game save.
#This will be updated in the last sprint.
knight_Points = 0
wizard_Points = 0
thief_Points = 0

hero_Points = 0
path_Name = os.path.dirname(os.path.abspath(__file__)) + "\Game_Save.csv"
with open(path_Name,"a") as file:
    file.close()
username = str(input("What is your username?\n-> "))
user_Info, found_Username = load_Game(username)
if found_Username == 1:
    print(user_Info)
    input("Press enter to continue!")

#While loop for Hero Choice.
while True:
    os.system("cls")
    game_meny(f"Welcome, {username}!")
    hero_Choice = int_input("What hero do you wanna play?\n1.Knight\n2.Wizard\n3.Thief\n-> ")
    os.system("cls")
    game_meny(f"Welcome, {username}")
    if hero_Choice == 1:
        print("--Knight--\nInitiative 5\nDurability 9\nAttack 6\nFlexibility 4\n"
        "\nThe knight's special ability is Shieldblock. Avoid damage on the first attack")
        answer = accepted_Hero_Input("Do you wanna play with the Knight? y/n \n->")
        hero = "Knight"
        hero_Object = hc.Knight()
        hero_Points = knight_Points
    
    if hero_Choice == 2:
        print("--Wizard--\nInitiative 6\nDurability 4\nAttack 9\nFlexibility 5\n"
        "\nThe wizard's special ability is Flash of Light. An 80% chance to escape from combat")
        answer = accepted_Hero_Input("Do you wanna play with the Wizard? y/n \n->")
        hero = "Wizard"
        hero_Object = hc.Wizard()
        hero_Points = wizard_Points
    
    if hero_Choice == 3:
        print("--Thief--\nInitiative 7\nDurability 5\nAttack 5 \nFlexability 7\n"
        "\nSpecial Ability: Critical Hit. The thief has 25% chance to do double damage with each attack.")
        answer = accepted_Hero_Input("Do you wanna play with the Thief? y/n \n->")
        hero = "Thief"
        hero_Object = hc.Thief()
        hero_Points = thief_Points

    if answer == "y":
        break
if hero_Points == 0:
    with open(path_Name,"a") as file:
        file.write(f"{username},{hero},{hero_Points}")
os.system("cls")
game_meny(f"Playing as {hero}!")

map_Choice = int_input("What map size do you wanna play?\n1.Small\n2.Medium\n3.Large\n-> ")

#Map Size will decide if it should be a 4x4, 5x5 or 8x8 map.

if map_Choice == 1:
    map_Size = 4
if map_Choice == 2:
    map_Size = 5
if map_Choice == 3:
    map_Size = 8

#Create the map and saves it to grid_map
grid_map = create_map(map_Size)
os.system("cls")
game_meny(f"Playing as {hero}!")

monster_Room_Dict = place_Monster(grid_map)
exit_Room_Dict = exit_Map(grid_map)
treasure_Room_Dict = place_Treasure(grid_map)
#While loop for
while True:
    right_input = ("1","2","3","4")
    
    start_pos_input = str(input("What corner you wanna start in?\n1.Top left\n2.Top right\n3.Bottom left\n4.Bottom right\n> "))
    
    if start_pos_input in right_input:
        #Sets the start pos, 4 diffrent cases.
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

# @ Symbol is for the hero, sets it to the start pos.
grid_map[start_pos_x,start_pos_y] = "@"
#Hero pos variable is for to check where the hero is.
hero_pos = [start_pos_x, start_pos_y]
#Will remove everything from the starter room.
try:
    del monster_Room_Dict[start_pos_x, start_pos_y]
except KeyError:
    pass
try:
    del exit_Room_Dict[start_pos_x, start_pos_y]
except KeyError:
    pass
try:
    del treasure_Room_Dict[start_pos_x, start_pos_y]
except KeyError:
    pass
#While loop for movement.
wrong_input = ""
while True:
    os.system("cls")
    game_meny(f"Health: {hero_Object.immunity} \t Points: {hero_Points}\n" + wrong_input)
    wrong_input = ""
    found_Room = 0
    print_map(grid_map,map_Size)

    #Open room will be an O.
    grid_map[hero_pos[0], hero_pos[1]] = "o"
    if (hero_pos[0], hero_pos[1]) in exit_Room_Dict.keys() or found_Room == 1:
        grid_map[hero_pos[0], hero_pos[1]] = "E"
        x = 1
    movement = str(input("Where do you wanna go?\n->"))
    old_Hero_Pos = [hero_pos[0],hero_pos[1]]

    if movement == "w":
        hero_pos[0] = hero_pos[0] - 1
    elif movement == "s":
        hero_pos[0] = hero_pos[0] + 1
    elif movement == "d":
        hero_pos[1] = hero_pos[1] + 1
    elif movement == "a":
        hero_pos[1] = hero_pos[1] - 1
    elif movement == "q":
        break
    else:
        wrong_input = "Use W for up, A for left, D for right, S for down.\n"
        grid_map[hero_pos[0], hero_pos[1]] = "@"
        continue
    
    #If the hero walk too far down.
    if hero_pos[0] > map_Size - 1:
       wrong_input = "You cant go that way!\n"
       hero_pos[0] = hero_pos[0] - 1
    #If the hero walk too far up.
    if hero_pos[0] < 0:
        wrong_input = "You cant go that way!\n"
        hero_pos[0] = hero_pos[0] + 1
    #If the hero walk too far right.
    if hero_pos[1] > map_Size - 1:
        wrong_input = "You cant go that way!\n"
        hero_pos[1] = hero_pos[1] - 1
    #If the hero walk too far left.
    if hero_pos[1] < 0:
        wrong_input = "You cant go that way!\n"
        hero_pos[1] = hero_pos[1] + 1
    #Puts @ where the hero is.
    else:
        grid_map[hero_pos[0], hero_pos[1]] = "@"
        hero_pos_Tuple = (hero_pos[0],hero_pos[1])
        flee_Bool = 0
        if hero_pos_Tuple in exit_Room_Dict:
            os.system("cls")
            game_meny(f"Health: {hero_Object.immunity}\n" + wrong_input)
            print_map(grid_map,map_Size) 

            print("You have found an exit...")          
            while True:
                answer = str(input("Do you wish to Exit? Y/N\n->")).lower()
                if answer == "n":
                    if hero_pos_Tuple in monster_Room_Dict:
                        try:
                            del monster_Room_Dict[hero_pos_Tuple]
                        except KeyError:
                            pass
                    if hero_pos_Tuple in treasure_Room_Dict:
                        try:
                            del treasure_Room_Dict[hero_pos_Tuple]
                        except KeyError:
                            pass                    
                    break
                elif answer == "y":
                    save_Game()
                    print("Goodbye!")
                    time.sleep(3)
                    sys.exit()
                    
        if hero_pos_Tuple in monster_Room_Dict:
            
            monster_Type = monster_Room_Dict[hero_pos[0], hero_pos[1]]
            monster_Object_List = []
            #Creates monster
            try:
                monster_Types = monster_Type.split(",")
                for monster in monster_Types:
                    if monster == "Spider":
                        monster_Object_List.append(create_Monster("Spider"))
                    if monster == "Skeleton":
                        monster_Object_List.append(create_Monster("Skeleton"))
                    if monster == "Orc":
                        monster_Object_List.append(create_Monster("Orc"))
                    if monster == "Troll":
                        monster_Object_List.append(create_Monster("Troll"))
            except:
                pass

            for count, monster_Object in enumerate(monster_Object_List):
                os.system("cls")
                if hero_pos_Tuple in treasure_Room_Dict:
                    game_meny(f"This room has these treasures: {treasure_Room_Dict[hero_pos_Tuple]}"
                    f"\n\t   This room has {len(monster_Types)} monsters: {monster_Type}")
                else:
                    game_meny(f"This room has {len(monster_Types)} monsters: {monster_Type}")

                print("You have encountered ", monster_Object.name)
                while True:
                    fight_Flee = str(input("Do you wanna Fight or Flee?\n->")).lower()
                    if fight_Flee == "fight":
                        #Will compare these later, highest starts battle.
                        hero_Total_Initiative = dice_Roll(hero_Object.initiative)
                        monster_Total_Initiative = dice_Roll(monster_Object.initiative)

                        if hero_Total_Initiative > monster_Total_Initiative:
                            #Hero start battle
                            loser_Battle = start_Battle("Hero", hero_Object, monster_Object)
                            break
                        else:
                            #Monster start battle
                            loser_Battle = start_Battle("Monster",hero_Object,monster_Object)
                            break
                    elif fight_Flee == "flee":
                        print("You choose to Flee!")
                        #Wizard special attack
                        if type(hero_Object) == hc.Wizard:
                            old_flex = hero_Object.flexibility
                            hero_Object.flexibility = 8
                            
                            flee_Bool = flee(hero_Object.flexibility)
                            hero_Object.flexibility = old_flex
                        else:
                            flee_Bool = flee(hero_Object.flexibility)
            
                        if flee_Bool == 1:
                            #If you fleed move you to the old room.
                            grid_map[old_Hero_Pos[0], old_Hero_Pos[1]] = "@"
                            grid_map[hero_pos[0], hero_pos[1]] = "x" 
                            hero_pos[0], hero_pos[1] = old_Hero_Pos[0], old_Hero_Pos[1]
                            input("Press enter to continue!")
                            break
                        else:
                            #Else start battle
                            x = input("\nYou failed to flee!\nPress enter to Fight!\n")
                            loser_Battle = start_Battle("Monster", hero_Object, monster_Object)
                            input("Press enter to continue!")
                            break
                    else:
                        print("Type in Fight or Flee!")
                if fight_Flee == "flee":
                    break
                
                if loser_Battle == "Hero":
                    #If Hero dies in battle.
                    print("Better luck next time.")
                    x = input()
                    save_Game()
                    sys.exit()
                else:
                    #Removes the killed monster from the monster room dict
                    monster_Room_Dict[hero_pos[0], hero_pos[1]] = monster_Room_Dict[hero_pos[0], hero_pos[1]].replace(monster_Object.name + ",", "", 1)
                    #If all monster are dead, go back to map
                    if count == len(monster_Object_List) - 1:
                        del monster_Room_Dict[hero_pos_Tuple]
                        x = input("Press enter to continue!")
                        break
                    x = input("Press enter to continue!")
        if hero_pos_Tuple in treasure_Room_Dict and flee_Bool == 0:
            os.system("cls")
            game_meny(f"\tTREASURES")
            treasures = treasure_Room_Dict[hero_pos_Tuple]
            treasures_Object_List = create_Treasure(treasures)
            print("Treasures: ")
            total_Points = 0
            for treasure in treasures_Object_List:
                print(f"{treasure.name}, Points: {treasure.points}")
                hero_Points = int(hero_Points) + treasure.points
                total_Points = total_Points + treasure.points
            print(f"You found a total of {total_Points} points!")
            del treasure_Room_Dict[hero_pos_Tuple]
            x = input("Press enter to go back to the map!")
            

