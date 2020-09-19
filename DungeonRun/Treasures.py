import random

class Treasure:
    def __init__(self,points,name):
        self.points = points
        self.name = name



"""
class Coin(Treasure):
    def __init__(self):
        super().__init__(
            
            points = 2
        )

class Money_Pouch(Treasure):
    def __init__(self):
        super().__init__(
            
            points = 6
        )      

class Gold(Treasure):
    def __init__(self):
        super().__init__(
            
            points = 10
        )

class Gemstone(Treasure):
    def __init__(self):
        super().__init__(
            
            points = 14            
        )

class Small_Chest(Treasure):
    def __init__(self):
        super().__init__(            
            points = 20
                )        


def drop_rate():

    treasure_List = []
    chance = random.randint(1,100)
    
    if chance <= 40 and chance > 1:
        treasure_List.append("Coin")
    if chance <= 20 and chance > 1:
        treasure_List.append("Money Pouch")
    if chance <= 15 and chance > 1:
        treasure_List.append("Gold")
    if chance <= 10 and chance > 1:
        treasure_List.append("GemStone")
    if chance <= 5 and chance > 1:
        treasure_List.append("Small Chest")
    
    return treasure_List
    
x = drop_rate()

print(x)
"""