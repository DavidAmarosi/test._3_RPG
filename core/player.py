import random
class Player:
    def __init__(self,name):
        self.name = name
        self.hp = 50
        self.speed = random.randint(5,10)
        self.power = random.randint(5,10)
        self.profession = random.choice(["fighter","cure"])
        self.armor_rating = random.randint(5,15)
        self.hps()
        self.powers()

    def hps(self):
        if self.profession == "cure":
            self.hp += 10

    def powers(self):
        if self.profession == "fighter":
            self.power +=2
    
    def speak(self): 
        print(f"the player {self.name} is won")

    def attack(self):
        pass





if __name__ == "__main__":
    player1 = Player("david")
    print(player1.profession)
    print(player1.profession)
    print(player1.hp)
    print(player1.power)
