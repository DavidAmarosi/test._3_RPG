from core.orc import Orc
from core.goblin import Goblin
from core.player import Player
import random
class Game(Orc,Goblin,Player):
    def start(self):
        
        if self.show_menu() == "y":
            monster = self.choose_random_monster()
            player = self.create_player()
            Monster_turn = monster.speed + self.roll_dice(6)
            Player_turn = player.speed + self.roll_dice(6)
            if Player_turn >=Monster_turn:
                validity = player
                attacked = monster


            if Player_turn < Monster_turn:
                validity = monster
                attacked = player

            self.battle(validity,attacked)
            
        else:
            print("The player doesn't want to play.")
        

    def show_menu(self):
        battles = input("Do you want to continue the fight or leave? y/n? ")
        return battles
      

    def create_player(self):
        player = Player("david")
        return player
        pass
    def choose_random_monster(self):
        monster = random.choice([Orc("wolf"),Goblin("bear")])
        return monster
      
    def battle(self,player, monster):
        attacked = player
        validity = monster
        Status_check = False
        while not Status_check:
            self.roll_dice(20)
            attack = validity.speed + 20
            if attack > attacked.armor_rating:
    
                if isinstance(validity ,Player):
                    validity.power+= self.roll_dice(6)
                    attacked.hp -= self.roll_dice(6)
                    
                else:
                    num1 = self.roll_dice(6)
                    if validity.profession == "sword":
                        num = num1 * 0.5
                    if validity.profession == "knife":
                        num = num1 * 1
                    if validity.profession == "ax":
                        num = num1 * 1.5

                    validity.power += num
                    attacked.hp -= num
                if attacked.hp <=0:
                    Status_check = True
                    print(Status_check)
                    print(validity.speak())
                    print(validity.profession)
                    


            else:
                validity, attacked = validity, attacked

       




    def roll_dice(self,sides):
        num = random.randint(1,sides)
        return num
    