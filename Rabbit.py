import random
class Rabbit:
    def __init__(self):
        self.isState_first = "Живой"
        self.isState_second = "Живой"

    def location_rabbits(self):
        while True:
            x1, y1 = random.randint(0, 4), random.randint(0, 4)
            x2, y2 = random.randint(0, 4), random.randint(0, 4)
            if (x1, y1) != (0, 0) and (x2, y2) != (0, 0) and (x1, y1) != (x2, y2):
                break
        return x1, y1, x2, y2


    def motion_detection_first(self, x1, y1):
        if x1 == 0 and y1 == 0:
            first_action = random.randint(2, 3)
        elif x1 == 0 and y1 == 4:
            first_action = random.randint(3, 4)
        elif x1 == 4 and y1 == 4:
            first_action = random.randint(1, 2)
            if first_action == 2:
                first_action = 4
        elif x1 == 4 and y1 == 0:
            first_action = random.randint(1, 2)
        elif x1 == 0 and y1 != 0 and y1 != 4:
            first_action = random.randint(2, 4)
        elif y1 == 4 and x1 != 0 and x1 != 4:
            first_action = random.randint(3, 5)
            if first_action == 5:
                first_action = 1
        elif x1 == 4 and y1 != 0 and y1 != 4:
            first_action = random.randint(1, 3)
            if first_action == 3:
                first_action = 4
        elif y1 == 0 and x1 != 0 and x1 != 4:
            first_action = random.randint(1, 3)
        else:
            first_action = random.randint(1, 4)
        return first_action

    def performing_the_movement_first(self, x1, y1, first_action):
        if first_action == 1:
            x1 -= 1
        elif first_action == 2:
            y1 += 1
        elif first_action == 3:
            x1 += 1
        else:
            y1 -= 1
        return x1, y1

    def motion_detection_second(self, x2, y2, x1, y1):
        while True:
            if x2 == 0 and y2 == 0:
                second_action = random.randint(2, 3)
            elif x2 == 0 and y2 == 4:
                second_action = random.randint(3, 4)
            elif x2 == 4 and y2 == 4:
                second_action = random.randint(1, 2)
                if second_action == 2:
                    second_action = 4
            elif x2 == 4 and y2 == 0:
                second_action = random.randint(1, 2)
            elif x2 == 0 and y2 != 0 and y2 != 4:
                second_action = random.randint(2, 4)
            elif y2 == 4 and x2 != 0 and x2 != 4:
                second_action = random.randint(3, 5)
                if second_action == 5:
                    second_action = 1
            elif x2 == 4 and y2 != 0 and y2 != 4:
                second_action = random.randint(1, 3)
                if second_action == 3:
                    second_action = 4
            elif y2 == 0 and x2 != 0 and x2 != 4:
                second_action = random.randint(1, 3)
            else:
                second_action = random.randint(1, 4)
            if second_action == 1:
                x2 -= 1
            elif second_action == 2:
                y2 += 1
            elif second_action == 3:
                x2 += 1
            else:
                y2 -= 1
            if x1 == x2 and y1 == y2:
                continue
            else:
                break
        return x2, y2