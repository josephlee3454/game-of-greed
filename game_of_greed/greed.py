import random
from collections import Counter


class GameLogic:
    @staticmethod
    def roll_dice(value):
        """RolL_Dice has one required parameter: value. Value is an integer for the number of dice to be rolled."""
        output = tuple()

        for i in range(value):
            num = random.randint(1, 6)
            output += (num,)
        return output

    @staticmethod
    def calculate_score(set_dice):  # example input = (1, 2, 3, 4, 5, 6)
        """Takes in tuple, evaluates game rules to calculate score"""
        score = 0
        current = Counter(
            set_dice
        )  # { 1:1 2:1 3:1 4:1 5:1 6:1 } { key : value } current[5] = 1
        common = Counter(set_dice).most_common(
            1
        )  # [(1, 1)] first most common in the set

        if len(current) == 0:
            return score

        if common[0][1] == 1 and len(current) == 6:
            score += 1500
            return score

        if common[0][1] == 2 and len(current) == 3:
            score += 1500
            return score

        for key in current:

            if key == 1:
                if current[key] == 3:
                    score += 1000
                elif current[key] == 4:
                    score += 2000
                elif current[key] == 5:
                    score += 3000
                elif current[key] == 6:
                    score += 4000
                else:
                    multiplier = current[key]
                    score += multiplier * 100
            if key == 2:
                if current[key] == 3:
                    score += 200
                elif current[key] == 4:
                    score += 400
                elif current[key] == 5:
                    score += 600
                elif current[key] == 6:
                    score += 800
                else:
                    pass

            if key == 3:
                if current[key] == 3:
                    score += 300
                elif current[key] == 4:
                    score += 600
                elif current[key] == 5:
                    score += 900
                elif current[key] == 6:
                    score += 1200
                else:
                    pass

            if key == 4:
                if current[key] == 3:
                    score += 400
                elif current[key] == 4:
                    score += 800
                elif current[key] == 5:
                    score += 1200
                elif current[key] == 6:
                    score += 1600
                else:
                    pass

            if key == 5:
                if current[key] == 3:
                    score += 500
                elif current[key] == 4:
                    score += 1000
                elif current[key] == 5:
                    score += 1500
                elif current[key] == 6:
                    score += 2000
                else:
                    multiplier = current[key]
                    score += multiplier * 50

            if key == 6:
                if current[key] == 3:
                    score += 600
                elif current[key] == 4:
                    score += 1200
                elif current[key] == 5:
                    score += 1800
                elif current[key] == 6:
                    score += 2400
                else:
                    pass
        return score


class Banker:
    def __init__(self, balance=0, shelved=0):
        self.balance = balance
        self.shelved = shelved

    def shelf(self, value):
        """Shelves the current score temporarily"""
        self.shelved += value

    def clear_shelf(self):
        """Resets shelf value to zero"""
        self.shelved = 0

    def bank(self):
        """Adds shelf value to balance"""
        self.balance += self.shelved
        return self.shelved
