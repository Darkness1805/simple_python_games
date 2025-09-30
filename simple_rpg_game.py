# make a game where the player can move around using wasd keys
# it has health and score system and enemies that move towards the player
# without using pygame  library
import random


class Player:
    def __init__(self, name):
        self.name = name
        self.health = random.randint(50, 150)
        self.score = 0
        self.position = [0, 0]  # x, y coordinates

    def move(self, direction):
        if direction == "w":
            self.position[1] += 2
        elif direction == "s":
            self.position[1] -= 2
        elif direction == "a":
            self.position[0] -= 2
        elif direction == "d":
            self.position[0] += 2

    def Attack(self, enemy):
        attack_power = random.randint(5, 25)
        if (
            abs(self.position[0] - enemy.position[0]) <= 3
            and abs(self.position[1] - enemy.position[1]) <= 3
        ):
            
            enemy.health -= attack_power
            self.score += attack_power
            print(f"Attacked enemy for {attack_power} damage!")

    def heal(self, amount):
        self.health += amount
        print(f"Healed for {amount} health!")
        self.score -= amount  

    def super_attack(self, enemy,score_to_atack):
        if (
            abs(self.position[0] - enemy.position[0]) <= 5 + score_to_atack/10
            and abs(self.position[1] - enemy.position[1]) <= 5 + score_to_atack/10
        ):
            power = 16 ** (score_to_atack // 100) 
            print(f"Super Attacked enemy for {power} damage!")
            enemy.health -= power
            if(self.score>=33):
                self.score -= score_to_atack 
            else:
                self.score = 0
            player.health -= power*0.001
            self.score += 30

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def display_status(self):
        print(
            f"Player: {self.name}, Health: {self.health}, Score: {self.score}, Position: {self.position}"
        )


class enamy:
    def __init__(self, position):
        self.health = random.randint(20, 100)
        self.position = position  # x, y coordinates
        self.speed = random.randint(1,3)

    def move_towards(self, player_position):
        
        if self.position[0] < player_position[0]:
            self.position[0] += self.speed
        elif self.position[0] > player_position[0]:
            self.position[0] -= self.speed

        if self.position[1] < player_position[1]:
            self.position[1] += self.speed
        elif self.position[1] > player_position[1]:
            self.position[1] -= self.speed

    def is_alive(self):
        if self.health > 0:
            return True
        return False
    def attack(self,player):
        attack_power = random.randint(1, 8)
        if (
            abs(self.position[0] - player.position[0]) <= 2
            and abs(self.position[1] - player.position[1]) <= 2
        ):
            print("Enemy Attacked!")
            player.health -= attack_power
            if player.health <= 0:
                print("Player defeated!")
                exit()
    
    def Explode(self,player):
        t = random.randint(1,20)
        if(self.health <= 30 and t <=2 ):
            print("Enemy Exploded!")
            player.health -= self.health*2
            self.health = 0
            if player.health <= 0:
                print("Player defeated!")
                exit()

    def display_status(self):
        print(f"Enemy Health: {self.health}, Position: {self.position},speed: {self.speed}")


def enemy_spawn(number_of_enemies,enemies_list):
    
    for _ in range(number_of_enemies):  # Create 3 enemies at random positions
      enemy_position = [random.randint(-20, 20), random.randint(-20, 20)]
      new_enemy = enamy(enemy_position)
      enemies_list.append(new_enemy)
      print(f"An enemy has appeared at position {enemy_position}!")

    return enemies_list



player_name = input("Enter your player's name: ")
player = Player(player_name)
number_of_enemies = random.randint(1, 7)
difficulty = input("Select difficulty (easy, medium, hard): ").lower()
if difficulty == "easy":
    number_of_enemies = 3
elif difficulty == "medium":
    number_of_enemies = max(5, number_of_enemies)
elif difficulty == "hard":
    number_of_enemies = random.randint(5, 5*number_of_enemies)
    player.health += number_of_enemies*10


enamies = enemy_spawn(number_of_enemies,[])

print( f'Game Start! {number_of_enemies} enemies approaching!')
      

while player.is_alive():
    random_lucky = random.randint(1, 10)
    health = [random.randint(-20, 20), random.randint(-20, 20)]
    if (random_lucky <=2):
        print("Lucky! You found a health pack. at ",health )
        player.health += 10
   
    if player.position == health:
        player.health += 10
        print("Health pack found! Health increased by 10.")
    player.display_status()

    for enemy in enamies:
        enemy.move_towards(player.position)
        enemy.attack(player)
        enemy.display_status()
    player.display_status()
    move = input("Move (w/a/s/d): ")
    player.move(move)
   
    if move == "r" or move == "t" or move == "h":
        if move == "h":
            heal_amount = input("Enter heal amount (10, 50, 100): ")
            if heal_amount in ["10", "50", "100"]:
                amount = (player.score/100)*int(heal_amount)
                player.heal(amount)
            else:
                print("Invalid heal amount.")
                continue
        attacked_in_turn = False
        ch_power = 0
        if move == "t":
                charger_power = input("Enter charge power 10 , 50 , 100: ")
                if charger_power == "10":
                    ch_power = player.score//10
                elif charger_power == "50":
                    ch_power = player.score//2
                elif charger_power == "100":
                    ch_power = player.score
                
        for enemy in enamies:
            if move == "r":
                player.Attack(enemy)
            elif move == "t" :
                player.super_attack(enemy,ch_power)
            
                
            enemy.Explode(player)
            if not enemy.is_alive():
                print("Enemy defeated!")
                enamies.remove(enemy)
            if enamies == []:
                phase = input("You cleared the phase! Do you want to continue to next phase? (y/n): ")
                if phase.lower() == "y":
                    number_of_enemies += 2
                    enemy_spawn(number_of_enemies,enamies)
                    print(f"Next phase started with {number_of_enemies} enemies!")
                else:
                    print("You Win!")
                    player.display_status()
                    exit()

    if move == "q":
        player.display_status()
        break


print("Game Over!")
print(f"Final Score: {player.score}")
