import random
class Orc:
    def __init__(self,name):
        self.name = name
        self.hp = 50
        self.type = "orc"
        self.speed = random.randint(5,10)
        self.power = random.randint(10,15)
        self.armor_rating = random.randint(2,8)
        self.profession = random.choice(["sword","knife","ax"])
      
    def speak(self):
        print(f"the orc {self.name} is won")
    
    def attack(self):
        pass
