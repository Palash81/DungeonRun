import random
class Hero:
    """
        Superclass for heroes, arguments are initiative, 
        immunity, attack, flexibility. This class got the flee func.
    """
    def __init__(self,initiative, immunity, attack, flexibility):
        self.initiative = initiative
        self.immunity = immunity
        self.attack = attack
        self.flexibility = flexibility
    
    def flee(self):
        rnd_int = random.randint(1,100)
        flee_Chance = self.flexibility * 10
        if rnd_int > flee_Chance:
            print("You failed to flee!")
        else:
            print("You fled!")

class Knight(Hero):
    def __init__(self):
        super().__init__(
            initiative = 5,
            immunity = 9,
            attack = 6,
            flexibility = 4,
        )

class Wizard(Hero):
    def __init__(self):
        super().__init__(
            initiative = 6,
            immunity = 4,
            attack = 9,
            flexibility = 5
        )
class Thief(Hero):
    def __init__(self):
        super().__init__(
            initiative = 7,
            immunity = 5,
            attack = 5,
            flexibility = 7
        )