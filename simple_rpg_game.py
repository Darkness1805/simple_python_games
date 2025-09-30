# make a game where the player can move around using wasd keys
# it has health and score system and enemies that move towards the player
# without using pygame  library
import random


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
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
        if (
            abs(self.position[0] - enemy.position[0]) <= 1
            and abs(self.position[1] - enemy.position[1]) <= 1
        ):
            enemy.health -= 10
            self.score += 10

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
        self.health = 50
        self.position = position  # x, y coordinates

    def move_towards(self, player_position):
        if self.position[0] < player_position[0]:
            self.position[0] += 1
        elif self.position[0] > player_position[0]:
            self.position[0] -= 1

        if self.position[1] < player_position[1]:
            self.position[1] += 1
        elif self.position[1] > player_position[1]:
            self.position[1] -= 1

    def is_alive(self):
        if self.health > 0:
            return True
        return False
    def attack(self,player):
        if (
            abs(self.position[0] - player.position[0]) <= 2
            and abs(self.position[1] - player.position[1]) <= 2
        ):
            print("Enemy Attacked!")
            player.health -= 2
            if player.health <= 0:
                print("Player defeated!")
                exit()
    
    def Explode(self,player):
        t = random.randint(1,10)
        if(self.health <= 30 and t <=2 ):
            print("Enemy Exploded!")
            player.health -= self.health*2
            self.health = 0
            if player.health <= 0:
                print("Player defeated!")
                exit()

    def display_status(self):
        print(f"Enemy Health: {self.health}, Position: {self.position}")


player_name = input("Enter your player's name: ")
player = Player(player_name)
number_of_enemies = random.randint(1, 7)
difficulty = input("Select difficulty (easy, medium, hard): ").lower()
if difficulty == "easy":
    number_of_enemies = 3
elif difficulty == "medium":
    number_of_enemies = max(5, number_of_enemies)
elif difficulty == "hard":
    number_of_enemies = 5*number_of_enemies
enemies = []

for _ in range(number_of_enemies):  # Create 3 enemies at random positions
    enemy_position = [random.randint(-20, 20), random.randint(-20, 20)]
    new_enemy = enamy(enemy_position)
    enemies.append(new_enemy)
    print(f"An enemy has appeared at position {enemy_position}!")

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

    for enemy in enemies:
        enemy.move_towards(player.position)
        enemy.attack(player)
        enemy.display_status()

    move = input("Move (w/a/s/d): ")
    player.move(move)
   
    if move == "r":
        attacked_in_turn = False
        for enemy in enemies:
            player.Attack(enemy)
            enemy.Explode(player)
            if not enemy.is_alive():
                print("Enemy defeated!")
                enemies.remove(enemy)
            if enemies == []:
                print("You Win!")
                player.display_status()
                exit()

    if move == "q":
        player.display_status()
        break


print("Game Over!")
