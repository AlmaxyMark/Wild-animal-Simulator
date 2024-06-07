from Rabbit import Rabbit
from Tiger import Tiger
from colorama import init, Fore
init(autoreset=True)
import random
import time
class Gaming:
    def __init__(self):
        self.quantity_of_rabbits = 2
        self.size = 5
        self.field = [[Fore.GREEN + '0' for _ in range(self.size)] for _ in range(self.size)]
        self.gaming_rabbits = Rabbit()
        self.gaming_tiger = Tiger()
        self.field[0][0] = Fore.RED + "Т"

    def location_of_the_animals(self):
        x1, y1, x2, y2 = self.gaming_rabbits.location_rabbits()
        self.field[x1][y1] = Fore.LIGHTWHITE_EX + "З"
        self.field[x2][y2] = Fore.LIGHTWHITE_EX + "З"
        self.gaming_rabbits.x1, self.gaming_rabbits.y1, self.gaming_rabbits.x2, self.gaming_rabbits.y2 = x1, y1, x2, y2


    def print_field(self):
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                print(self.field[i][j], end=" ")
            print()
        time.sleep(1)

    def proximity_check(self):
        x, y = self.gaming_tiger.x, self.gaming_tiger.y
        x1, y1, x2, y2 = self.gaming_rabbits.x1, self.gaming_rabbits.y1, self.gaming_rabbits.x2, self.gaming_rabbits.y2
        if (x == x1 and abs(y - y1) == 1) or (y == y1 and abs(x - x1) == 1):
            self.gaming_tiger.isState = "Атаковать добычу"
            chance = self.gaming_tiger.attack_rabbit()
            print(Fore.LIGHTYELLOW_EX + "Тигр атакует добычу")
            time.sleep(2)
            if chance == 1:
                self.field[x][y] = Fore.GREEN + '0'
                self.field[x1][y1] = Fore.RED + "Т"
                self.gaming_tiger.x, self.gaming_tiger.y = x1, y1
                self.gaming_rabbits.isState_first = "Неживой"
                self.print_field()
                print(Fore.LIGHTGREEN_EX + "Тигр успешно атаковал добычу")
                time.sleep(2)
                self.gaming_tiger.isState = "Бежать домой"
                self.field[x1][y1] = Fore.GREEN + '0'
                self.field[0][0] = Fore.RED + "Т"
                self.print_field()
                return self.gaming_tiger.isState
            else:
                self.field[x1][y1] = Fore.GREEN + '0'
                x1, y1 = self.the_rebound_of_the_rabbit_first()
                self.field[x1][y1] = Fore.LIGHTWHITE_EX + "З"
                self.gaming_rabbits.x1, self.gaming_rabbits.y1 = x1, y1
                self.print_field()
                print(Fore.RED + "Тигр неудачно атаковал добычу")
                time.sleep(2)
                self.gaming_tiger.isState = "Выследить добычу"
                return self.gaming_tiger.isState
        elif (x == x2 and abs(y - y2) == 1) or (y == y2 and abs(x - x2) == 1):
            self.gaming_tiger.isState = "Атаковать добычу"
            chance = self.gaming_tiger.attack_rabbit()
            print(Fore.LIGHTYELLOW_EX + "Тигр атакует добычу")
            time.sleep(2)
            if chance == 1:
                self.field[x][y] = Fore.GREEN + '0'
                self.field[x2][y2] = Fore.RED + "Т"
                self.gaming_tiger.x, self.gaming_tiger.y = x2, y2
                self.gaming_rabbits.isState_second = "Неживой"
                self.print_field()
                print(Fore.LIGHTGREEN_EX + "Тигр успешно атаковал добычу")
                time.sleep(2)
                self.gaming_tiger.isState = "Бежать домой"
                self.field[x2][y2] = Fore.GREEN + '0'
                self.field[0][0] = Fore.RED + "Т"
                self.print_field()
                return self.gaming_tiger.isState
            else:
                self.field[x2][y2] = Fore.GREEN + '0'
                x2, y2 = self.the_rebound_of_the_rabbit_second()
                self.field[x2][y2] = Fore.LIGHTWHITE_EX + "З"
                self.gaming_rabbits.x2, self.gaming_rabbits.y2 = x2, y2
                self.print_field()
                print(Fore.RED + "Тигр неудачно атаковал добычу")
                time.sleep(2)
                self.gaming_tiger.isState = "Выследить добычу"
                return self.gaming_tiger.isState
        else:
            print(Fore.CYAN + "Тигр выслеживает добычу")
            time.sleep(2)

    def processing_the_movement_of_rabbits_first(self):
        x1, y1, x2, y2 = self.gaming_rabbits.x1, self.gaming_rabbits.y1, self.gaming_rabbits.x2, self.gaming_rabbits.y2
        self.field[x1][y1] = Fore.GREEN + '0'
        self.field[x2][y2] = Fore.GREEN + '0'

    def processing_the_movement_of_rabbits_second(self):
        x1, y1, x2, y2 = self.gaming_rabbits.x1, self.gaming_rabbits.y1, self.gaming_rabbits.x2, self.gaming_rabbits.y2
        self.field[x1][y1] = Fore.LIGHTWHITE_EX + "З"
        self.field[x2][y2] = Fore.LIGHTWHITE_EX + "З"

    def processing_the_movement_of_tiger_first(self):
        x, y = self.gaming_tiger.x, self.gaming_tiger.y
        self.field[x][y] = Fore.GREEN + '0'

    def processing_the_movement_of_tiger_second(self):
        x, y = self.gaming_tiger.x, self.gaming_tiger.y
        if 0 <= x < self.size and 0 <= y < self.size:
            self.field[x][y] = Fore.RED + "Т"

    def the_rebound_of_the_rabbit_first(self):
        rebound = 0
        x1, y1 = self.gaming_rabbits.x1, self.gaming_rabbits.y1
        x, y = self.gaming_tiger.x, self.gaming_tiger.y
        if 1 <= x1 <= 3 and 1 <= y1 <= 3:
            if x - x1 == 1 and y == y1:
                rebound = random.randint(1, 3)
                if rebound == 3:
                    rebound = 4
            elif x == x1 and y1 - y == 1:
                rebound = random.randint(1, 3)
            elif x1 - x == 1 and y == y1:
                rebound = random.randint(1, 3)
                if rebound == 1:
                    rebound = 4
            elif x == x1 and y - y1 == 1:
                rebound = random.randint(1, 3)
                if rebound == 2:
                    rebound = 4
        elif x1 == 0 and 1 <= y1 <= 3:
            if x1 == x and y - y1 == 1:
                rebound = random.randint(3, 4)
            elif x - x1 == 1 and y == y1:
                rebound = random.randint(1, 2)
                if rebound == 1:
                    rebound = 4
            elif x == x1 and y1 - y == 1:
                rebound = random.randint(2, 3)
        elif 1 <= x1 <= 3 and y1 == 4:
            if x - x1 == 1 and y == y1:
                rebound = random.randint(1, 2)
                if rebound == 2:
                    rebound = 4
            elif x == x1 and y1 - y == 1:
                rebound = random.randint(1, 2)
                if rebound == 2:
                    rebound = 3
            elif x1 - x == 1 and y == y1:
                rebound = random.randint(3, 4)
        elif x1 == 4 and 1 <= y1 <= 3:
            if x == x1 and y1 - y == 1:
                rebound = random.randint(1, 2)
            elif x1 - x == 1 and y == y1:
                rebound = random.randint(1, 2)
                if rebound == 1:
                    rebound = 4
            elif x == x1 and y - y1 == 1:
                rebound = random.randint(1, 2)
                if rebound == 2:
                    rebound = 4
        elif 1 <= x1 <= 3 and y1 == 0:
            if x1 - x == 1 and y == y1:
                rebound = random.randint(2, 3)
            elif x == x1 and y - y1 == 1:
                rebound = random.randint(1, 2)
                if rebound == 2:
                    rebound = 3
            elif x - x1 == 1 and y == y1:
                rebound = random.randint(1, 2)
        elif x1 == 0 and y1 == 0:
            if x == 1 and y == 0:
                rebound = 2
            elif x == 0 and y == 1:
                rebound = 3
        elif x1 == 0 and y1 == 4:
            if x == 0 and y == 3:
                rebound = 3
            elif x == 1 and y == 4:
                rebound = 4
        elif x1 == 4 and y1 == 4:
            if x == 3 and y == 4:
                rebound = 4
            elif x == 4 and y == 3:
                rebound = 1
        elif x1 == 4 and y1 == 0:
            if x == 3 and y == 0:
                rebound = 2
            elif x == 4 and y == 1:
                rebound = 1
        if rebound == 1:
            x1 -= 1
        elif rebound == 2:
            y1 += 1
        elif rebound == 3:
            x1 += 1
        else:
            y1 -= 1
        return x1, y1

    def the_rebound_of_the_rabbit_second(self):
        rebound = 0
        x2, y2, x1, y1 = self.gaming_rabbits.x2, self.gaming_rabbits.y2, self.gaming_rabbits.x1, self.gaming_rabbits.y1
        x, y = self.gaming_tiger.x, self.gaming_tiger.y
        while True:
            if 1 <= x2 <= 3 and 1 <= y2 <= 3:
                if x - x2 == 1 and y == y2:
                    rebound = random.randint(1, 3)
                    if rebound == 3:
                        rebound = 4
                elif x == x2 and y2 - y == 1:
                    rebound = random.randint(1, 3)
                elif x2 - x == 1 and y == y2:
                    rebound = random.randint(1, 3)
                    if rebound == 1:
                        rebound = 4
                elif x == x2 and y - y2 == 1:
                    rebound = random.randint(1, 3)
                    if rebound == 2:
                        rebound = 4
            elif x2 == 0 and 1 <= y2 <= 3:
                if x2 == x and y - y2 == 1:
                    rebound = random.randint(3, 4)
                elif x - x2 == 1 and y == y2:
                    rebound = random.randint(1, 2)
                    if rebound == 1:
                        rebound = 4
                elif x == x2 and y2 - y == 1:
                    rebound = random.randint(2, 3)
            elif 1 <= x2 <= 3 and y2 == 4:
                if x - x2 == 1 and y == y2:
                    rebound = random.randint(1, 2)
                    if rebound == 2:
                        rebound = 4
                elif x == x2 and y2 - y == 1:
                    rebound = random.randint(1, 2)
                    if rebound == 2:
                        rebound = 3
                elif x2 - x == 1 and y == y2:
                    rebound = random.randint(3, 4)
            elif x2 == 4 and 1 <= y2 <= 3:
                if x == x2 and y2 - y == 1:
                    rebound = random.randint(1, 2)
                elif x2 - x == 1 and y == y2:
                    rebound = random.randint(1, 2)
                    if rebound == 1:
                        rebound = 4
                elif x == x2 and y - y2 == 1:
                    rebound = random.randint(1, 2)
                    if rebound == 2:
                        rebound = 4
            elif 1 <= x2 <= 3 and y2 == 0:
                if x2 - x == 1 and y == y2:
                    rebound = random.randint(2, 3)
                elif x == x2 and y - y2 == 1:
                    rebound = random.randint(1, 2)
                    if rebound == 2:
                        rebound = 3
                elif x - x2 == 1 and y == y2:
                    rebound = random.randint(1, 2)
            elif x2 == 0 and y2 == 0:
                if x == 1 and y == 0:
                    rebound = 2
                elif x == 0 and y == 1:
                    rebound = 3
            elif x2 == 0 and y2 == 4:
                if x == 0 and y == 3:
                    rebound = 3
                elif x == 1 and y == 4:
                    rebound = 4
            elif x2 == 4 and y2 == 4:
                if x == 3 and y == 4:
                    rebound = 4
                elif x == 4 and y == 3:
                    rebound = 1
            elif x2 == 4 and y2 == 0:
                if x == 3 and y == 0:
                    rebound = 2
                elif x == 4 and y == 1:
                    rebound = 1
            if rebound == 1:
                x2 -= 1
            elif rebound == 2:
                y2 += 1
            elif rebound == 3:
                x2 += 1
            else:
                y2 -= 1
            if x1 == x2 and y1 == y2:
                continue
            else:
                break
        return x2, y2

    def simulate(self):
        self.location_of_the_animals()
        self.print_field()
        if self.proximity_check() == "Атаковать добычу":
            print(Fore.LIGHTYELLOW_EX + "Тигр атакует добычу")
            time.sleep(2)
        while self.gaming_tiger.isState != "Бежать домой":
            self.processing_the_movement_of_rabbits_first()
            action_first = self.gaming_rabbits.motion_detection_first(self.gaming_rabbits.x1, self.gaming_rabbits.y1)
            self.gaming_rabbits.x1, self.gaming_rabbits.y1 = self.gaming_rabbits.performing_the_movement_first(self.gaming_rabbits.x1, self.gaming_rabbits.y1, action_first)
            self.gaming_rabbits.x2, self.gaming_rabbits.y2 = self.gaming_rabbits.motion_detection_second(self.gaming_rabbits.x2, self.gaming_rabbits.y2, self.gaming_rabbits.x1, self.gaming_rabbits.y1)
            self.processing_the_movement_of_rabbits_second()
            self.print_field()
            self.proximity_check()
            if self.gaming_tiger.isState == "Бежать домой":
                print(Fore.LIGHTMAGENTA_EX + "Игра завершена. Тигр вернулся домой.")
                break
            self.processing_the_movement_of_tiger_first()
            self.gaming_tiger.x, self.gaming_tiger.y = self.gaming_tiger.find_rabbit(self.gaming_tiger.x, self.gaming_tiger.y)
            self.processing_the_movement_of_tiger_second()
            self.print_field()
            self.proximity_check()
            if self.gaming_tiger.isState == "Бежать домой":
                print(Fore.LIGHTMAGENTA_EX + "Игра завершена. Тигр вернулся домой.")
                break
game = Gaming()
game.simulate()