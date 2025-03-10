import random

class Robot:
    def __init__(self, name, hp, attack_power, defense):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.defense = defense

    def attack_enemy(self, enemy):
        if random.random() < 0.2:  # 20% chance to miss
            print(f"{self.name} gagal menyerang!")
        else:
            damage = max(0, self.attack_power - enemy.defense)
            if random.random() < 0.1:  # 10% chance for critical hit
                damage *= 2
                print("Serangan kritikal!")
            enemy.hp -= damage
            print(f"{self.name} menyerang {enemy.name} dan menyebabkan {damage} damage!")

    def is_alive(self):
        return self.hp > 0

class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.round_number = 1

    def play(self):
        while self.robot1.is_alive() and self.robot2.is_alive():
            print(f"\nRound-{self.round_number} ==================================================")
            print(f"{self.robot1.name} [{self.robot1.hp}|{self.robot1.attack_power}]")
            print(f"{self.robot2.name} [{self.robot2.hp}|{self.robot2.attack_power}]")
            
            action1 = self.get_action(self.robot1)
            action2 = self.get_action(self.robot2)
            
            if action1 == 3:
                print(f"{self.robot1.name} menyerah!")
                print(f"{self.robot2.name} menang!")
                return
            if action2 == 3:
                print(f"{self.robot2.name} menyerah!")
                print(f"{self.robot1.name} menang!")
                return
            
            if action1 == 1:
                self.robot1.attack_enemy(self.robot2)
            if action2 == 1:
                self.robot2.attack_enemy(self.robot1)
            
            self.round_number += 1
        
        self.declare_winner()

    def get_action(self, robot):
        while True:
            try:
                action = int(input(f"{robot.name}, pilih aksi (1. Attack  2. Defense  3. Giveup): "))
                if action in [1, 2, 3]:
                    return action
            except ValueError:
                pass
            print("Masukkan pilihan yang valid!")

    def declare_winner(self):
        if self.robot1.is_alive():
            print(f"{self.robot1.name} menang!")
        else:
            print(f"{self.robot2.name} menang!")

# Contoh penggunaan
robot1 = Robot("Atreus", 500, 50, 10)
robot2 = Robot("Daedalus", 750, 40, 15)
game = Game(robot1, robot2)
game.play()
