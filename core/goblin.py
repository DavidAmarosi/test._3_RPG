import random
class Goblin:
    def __init__(self,name):
        self.name = name
        self.hp = 20
        self.type = "Goblin"
        self.speed = random.randint(5,10)
        self.power = random.randint(5,10)
        self.profession = random.choice(["sword","knife","ax"])
        self.armor_rating = 1
   
        
       
      
        pass
    def speak(self):
        print(f"the Goblin {self.name} is won")
    
    def attack(self):
        pass