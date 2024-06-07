import random
class Tiger:
    def __init__(self):
        self.isState = "Выследить добычу"
        self.x = 0
        self.y = 0
        
    def find_rabbit(self, x, y):
        if x == 0 and y == 0:
            tiger_action = random.randint(2, 3)
        elif x == 0 and y == 4:
            tiger_action = random.randint(3, 4)
        elif x == 4 and y == 4:
            tiger_action = random.randint(1, 2)
            if tiger_action == 2:
                tiger_action = 4
        elif x == 4 and y == 0:
            tiger_action = random.randint(1, 2)
        elif x == 0 and y != 0 and y != 4:
            tiger_action = random.randint(2, 4)
        elif y == 4 and x != 0 and x != 4:
            tiger_action = random.randint(3, 5)
            if tiger_action == 5:
                tiger_action = 1
        elif x == 4 and y != 0 and y != 4:
            tiger_action = random.randint(1, 3)
            if tiger_action == 3:
                tiger_action = 4
        elif y == 0 and x != 0 and x != 4:
            tiger_action = random.randint(1, 3)
        else:
            tiger_action = random.randint(1, 4)
        new_x, new_y = x, y
        if tiger_action == 1:
            new_x -= 1
        elif tiger_action == 2:
            new_y += 1
        elif tiger_action == 3:
            new_x += 1
        elif tiger_action == 4:
            new_y -= 1
        if 0 <= new_x < 5 and 0 <= new_y < 5:
            return new_x, new_y
        else:
            self.find_rabbit()

    def attack_rabbit(self):
        chance = random.randint(0, 1)
        return chance