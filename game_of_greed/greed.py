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
    def calculate_score(set_dice):  
        """Takes in tuple, evaluates game rules to calculate score"""
        score = 0
        current = Counter(set_dice) 
        common = Counter(set_dice).most_common(1)  

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


class Game:
    def __init__(self, roller=None):
        self.roller = roller
        self.rounds = 1
        self.dice_count = 6
        self.bank = Banker()

    def intro(self):
        """prints game introduction to user in command line"""
        print("Welcome to Game of Greed")
        response = input("Wanna play?")

        if response == "y":
            self.start_round(self.rounds, self.dice_count)
        else:
            print("OK. Maybe another time")

    def start_round(self, rounds, rolls):
        """initiates round of dice roll"""
        print(f"Starting round {rounds}")
        print(f"Rolling {rolls} dice...")

        if self.roller:
            dice_set = self.roller(rolls)
            print(self.dice_format(dice_set))
        else:
            dice_set = GameLogic.roll_dice(rolls)
            print(self.dice_format(dice_set))

        response = input("Enter dice to keep (no spaces), or (q)uit: ")
        if response == "q":
            print(f"Total score is {self.bank.balance} points")
            print(f"Thanks for playing. You earned {self.bank.balance} points")
        else:
            self.parse_input(response, rolls, dice_set)

    def dice_format(self, roll):
        """removes parenthesis and commas from string adds a comma between values"""
        return ",".join([str(i) for i in roll])

    def parse_input(self, response, rolls, dice_set):
        """converts user input to a tuple"""
        keepers = tuple([int(i) for i in response])
        if self.cheater_fix(dice_set, keepers):
            current_score = GameLogic.calculate_score(keepers)
            self.bank.shelf(current_score)
            remainder = rolls - len(keepers)

            print(
                f"You have {self.bank.shelved} unbanked points and {remainder} dice remaining"
            )
            response2 = input("(r)oll again, (b)ank your points or (q)uit ")
            if response2 == "q":
                print(f"Total score is {self.bank.balance} points")
                print(f"Thanks for playing. You earned {self.bank.balance} points")
            elif response2 == "r":
                self.rounds += 1
                self.dice_count -= len(keepers)
                self.start_round(self.rounds, self.dice_count)
            elif response2 == "b":
                banked_points = self.bank.bank()
                print(f"You banked {banked_points} points in round {self.rounds}")
                print(f"Total score is {self.bank.balance} points")
                self.bank.clear_shelf()
                self.rounds += 1
                self.dice_count = 6
                self.start_round(self.rounds, self.dice_count)
        else:
            print("Cheater!!! Or possibly made a typo...")
            print(self.dice_format(dice_set))
            new_response = input("Enter dice to keep (no spaces), or (q)uit: ")
            if response == "q":
                print(f"Total score is {self.bank.balance} points")
                print(f"Thanks for playing. You earned {self.bank.balance} points")
            else:
                self.parse_input(new_response, rolls, dice_set)

    def cheater_fix(self, dice_seq, userInput):  # dice_seq= (1, 2, 5, 5, 3, 4) userInput = (5, 5, 5) /or/ (6,7)
        """Testing user input against dice sequence"""
        dice_list = list(dice_seq)
        status = True
        for die in userInput:
            try:
                dice_list.pop(dice_list.index(die))
            except ValueError:
                status = False
        return status

    def play(self):
        """starts game"""
        self.intro()


if __name__ == "__main__":
    game = Game()
    game.play()
