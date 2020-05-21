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
    def calculate_score(set_dice, hot_dice_list):
        """Takes in tuple, evaluates game rules to calculate score"""

        score = 0
        current = Counter(set_dice)
        common = Counter(set_dice).most_common(1)

        if len(current) == 0:
            return score, hot_dice_list

        if common[0][1] == 1 and len(current) == 6:
            score += 1500
            hot_dice_list = []
            return score, hot_dice_list

        if common[0][1] == 2 and len(current) == 3:
            score += 1500
            hot_dice_list = []
            return score, hot_dice_list

        for key in current:

            if key == 1:
                if current[key] == 3:
                    score += 1000
                    filter((1), hot_dice_list)
                elif current[key] == 4:
                    score += 2000
                    filter((1), hot_dice_list)
                elif current[key] == 5:
                    score += 3000
                    filter((1), hot_dice_list)
                elif current[key] == 6:
                    score += 4000
                    filter((1), hot_dice_list)
                else:
                    multiplier = current[key]
                    score += multiplier * 100
                    filter((1), hot_dice_list)

            if key == 2:
                if current[key] == 3:
                    score += 200
                    current[key] = 0
                    filter((2), hot_dice_list)
                elif current[key] == 4:
                    score += 400
                    current[key] = 0
                    filter((2), hot_dice_list)
                elif current[key] == 5:
                    score += 600
                    current[key] = 0
                    filter((2), hot_dice_list)
                elif current[key] == 6:
                    score += 800
                    current[key] = 0
                    filter((2), hot_dice_list)
                else:
                    pass

            if key == 3:
                if current[key] == 3:
                    score += 300
                    current[key] = 0
                    filter((3), hot_dice_list)
                elif current[key] == 4:
                    score += 600
                    current[key] = 0
                    filter((3), hot_dice_list)
                elif current[key] == 5:
                    score += 900
                    current[key] = 0
                    filter((3), hot_dice_list)
                elif current[key] == 6:
                    score += 1200
                    current[key] = 0
                    filter((3), hot_dice_list)
                else:
                    pass

            if key == 4:
                if current[key] == 3:
                    score += 400
                    current[key] = 0
                    filter((4), hot_dice_list)
                elif current[key] == 4:
                    score += 800
                    current[key] = 0
                    filter((4), hot_dice_list)
                elif current[key] == 5:
                    score += 1200
                    current[key] = 0
                    filter((4), hot_dice_list)
                elif current[key] == 6:
                    score += 1600
                    current[key] = 0
                    filter((4), hot_dice_list)
                else:
                    pass

            if key == 5:
                if current[key] == 3:
                    score += 500
                    current[key] = 0
                    filter((5), hot_dice_list)
                elif current[key] == 4:
                    score += 1000
                    current[key] = 0
                    filter((5), hot_dice_list)
                elif current[key] == 5:
                    score += 1500
                    current[key] = 0
                    filter((5), hot_dice_list)
                elif current[key] == 6:
                    score += 2000
                    current[key] = 0
                    filter((5), hot_dice_list)
                else:
                    multiplier = current[key]
                    score += multiplier * 50
                    current[key] = 0

            if key == 6:
                if current[key] == 3:
                    score += 600
                    filter((6), hot_dice_list)
                elif current[key] == 4:
                    score += 1200
                    filter((6), hot_dice_list)
                elif current[key] == 5:
                    score += 1800
                    filter((6), hot_dice_list)
                elif current[key] == 6:
                    score += 2400
                    filter((6), hot_dice_list)
                else:
                    pass

        return score, hot_dice_list

    @staticmethod
    def get_scorers(dice):
        """Imported from client code, to make client provided bot work. // Regular game does not utilizet his code"""
        all_dice_score, _ = GameLogic.calculate_score(dice, [])

        if all_dice_score == 0:
            return tuple()

        scorers = []

        for i in range(len(dice)):
            sub_roll = dice[:i] + dice[i + 1 :]
            sub_score, _ = GameLogic.calculate_score(sub_roll, [])

            if sub_score != all_dice_score:
                scorers.append(dice[i])

        return tuple(scorers)

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
    def __init__(self, roller=None, num_rounds=16):
        self.roller = roller or GameLogic.roll_dice
        self.rounds = 1
        self.dice_count = 6
        self.dice_set = tuple()
        self.bank = Banker()
        self.num_rounds = num_rounds

    def intro(self):
        """prints game introduction to user in command line"""
        print("Welcome to Game of Greed")
        response = input("Wanna play?")

        if response == "y":
            self.start_round(self.rounds)
        else:
            print("OK. Maybe another time")

    def start_round(self, rounds):
        """initiates round of dice roll"""
        while self.rounds <= self.num_rounds:
            if self.dice_count == 6 and self.bank.shelved == 0:
                print(f"Starting round {self.rounds}")
            print(f"Rolling {self.dice_count} dice...")
            self.dice_set = self.roller(self.dice_count)  # dice set is created here
            print(self.dice_format(self.dice_set))

            score, _ = GameLogic.calculate_score(self.dice_set, list(self.dice_set))
            if score == 0:
                self.zilch()
            else:
                response = input("Enter dice to keep (no spaces), or (q)uit: ")
                if response == "q":
                    self.quit_game()
                else:
                    self.parse_input(response)
        self.quit_game()

    def dice_format(self, roll):
        """removes parenthesis and commas from string adds a comma between values"""
        return ",".join([str(i) for i in roll])

    def parse_input(self, response):
        """converts user input to a tuple"""
        keepers = tuple([int(i) for i in response])
        if self.cheater_fix(self.dice_set, keepers):
            current_score, hot_dice_list = GameLogic.calculate_score(
                keepers, list(keepers)
            )
            self.bank.shelf(current_score)
            remainder = self.dice_count - len(keepers)

            if len(keepers) == 6 and len(hot_dice_list) == 0:
                self.hot_dice(remainder, keepers)
            else:
                print(
                    f"You have {self.bank.shelved} unbanked points and {remainder} dice remaining"
                )
                response2 = input("(r)oll again, (b)ank your points or (q)uit ")
                if response2 == "q":
                    self.quit_game()
                elif response2 == "r":
                    self.dice_count -= len(keepers)
                    self.start_round(self.rounds)
                elif response2 == "b":
                    self.bank_round()

    def hot_dice(self, remainder, keepers):
        """confirming all dice were scoring dice against users kept list"""
        print(
            f"You have {self.bank.shelved} unbanked points and {remainder} dice remaining"
        )
        response2 = input("(r)oll again, (b)ank your points or (q)uit ")
        if response2 == "q":
            self.quit_game()
        elif response2 == "r":
            self.dice_count = 6
            self.start_round(self.rounds)
        elif response2 == "b":
            self.bank_round()

    def quit_game(self):
        """Quit the game. This will end the current game and print total score along with thanking the user."""
        print(f"Total score is {self.bank.balance} points")
        print(f"Thanks for playing. You earned {self.bank.balance} points")

    def bank_round(self):
        """Bank the current points in shelve along with print user friendly messages"""
        banked_points = self.bank.bank()
        print(f"You banked {banked_points} points in round {self.rounds}")
        print(f"Total score is {self.bank.balance} points")
        self.bank.clear_shelf()
        self.rounds += 1
        self.dice_count = 6
        self.start_round(self.rounds)

    def zilch(self):
        """Zilch! Ends the round, user turn, and starts the next round when a roll results in a score of 0"""
        print("Zilch!!! Round over")
        print(f"You banked 0 points in round {self.rounds}")
        print(f"Total score is {self.bank.balance} points")
        self.bank.clear_shelf()
        self.rounds += 1
        self.dice_count = 6
        self.start_round(self.rounds)

    def cheater_fix(self, dice_seq, userInput):
        """Testing user input against dice sequence"""
        dice_list = list(dice_seq)
        status = True
        for die in userInput:
            try:
                dice_list.pop(dice_list.index(die))
            except ValueError:
                status = False

        if status is not True:
            print("Cheater!!! Or possibly made a typo...")
            print(self.dice_format(self.dice_set))
            new_response = input("Enter dice to keep (no spaces), or (q)uit: ")
            if new_response == "q":
                self.quit_game()
            else:
                self.parse_input(new_response)
        else:
            return True

    def play(self):
        """starts game"""
        self.intro()


if __name__ == "__main__":
    game = Game()
    game.play()
