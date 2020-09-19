import random


class Monster:
    def __init__(self,initiative,immunity,attack,flexibility,rate,name):
        self.initiative = initiative
        self.immunity = immunity
        self.attack = attack
        self.flexibility = flexibility
        self.rate = rate
        self.name = name
    def spawn_rate(self):
        rnd_int = random.randint(1,50)
        if rnd_int <= 20 and rnd_int > 1:
            print("Spider")
        elif rnd_int <= 35 and rnd_int > 21:
            print("Skeleton")
        elif rnd_int <= 45  and rnd_int > 36:
            print("skeleton")
        else:
            print("troll")           


class Spider(Monster):
    def __init__(self):
        super().__init__(
        initiative = 7,
        immunity = 1,
        attack = 2,
        flexibility = 3,
        rate = 20,
        name = "Spider")

class Skeleton(Monster):
    def __init__(self):
        super().__init__(
        initiative = 4,
        immunity = 2,
        attack = 3,
        flexibility = 3,
        rate = 15,
        name = "Skeleton"
        )

class Orc(Monster):
    def __init__(self):
        super().__init__(
        initiative = 6,
        immunity = 3,
        attack = 4,
        flexibility = 4,
        rate = 10,
        name = "Orc")

class Troll(Monster):
    def __init__(self):
        super().__init__(
        initiative = 2,
        immunity = 4,
        attack = 7,
        flexibility = 2,
        rate = 5,
        name = "Troll")




             

        
        
        
        





    
    


        
        