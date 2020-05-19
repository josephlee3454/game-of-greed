# Lab: Class 06 - Class 09 Greed Game

## Open Git Pull Requests  

## Overview  
This project is a command line version of the dice game *Greed* using core Python tools and understanding of the basics of the language. The game is also known as Ten Thousand, Zilch, or Foo.  

## Feature Tasks and Requirements  
### Class 06 Greed Part 1  
- Today is all about assessing the highest risk features and formulating a plan.  
- The features we will focus on are <b>game logic</b> and the <b>tracking points</b>.  
    - [x] Define a GameLogic class to calculate score for a dice roll.  
        - [x] add `calculate_score` static method.  
        - [x] The input to `calculate_score` is a tuple of integers that represents a dice roll.  
        - [x] The output from `calculate_score` is an integer representing the roll's score according to <b>rules of game</b>.  
        - There are a lot of rules, write tests for different "kinds" of roles  
            - This will require skill in determining how many tests are enough.  
            - If you tried to test every scenario the number of tests would be massive.  
    - Handling rolling dice  
      - [x] Add `roll_dice` static method to GameLogic class.  
      - [x] The input to `roll_dice` is an integer between 1 and 6.  
      - [x] The output of `roll_dice` is a tuple with random values between 1 and 6.  
      - [x] The length of tuple must match the argument given to `roll_dice` method.  
    - Handle banking points  
      - [x] Define a Banker class  
      - [ ] Add a `shelf` instance method  
        - [ ] Input to `shelf` is the amount of points(integer) to add to shelf.  
        - [ ] `shelf` should temporarily store <b>unbanked</b> points.  
      - [ ] Add a `bank` instance method  
        - [ ] `bank` should add any points on the <b>shelf</b> to total and reset shelf to 0  
        - [ ] `bank` output should be the amount of points added to total from shelf  
      - [ ] Add a `clear_shelf` instance method  
        - [ ] `clear_shelf` should remove all unbanked points.

## User Acceptance Tests  
### Testing - Roll Dice
- [ ] When rolling 1 to 6 dice ensure:
  - [ ] A sequence of correct length is returned  
  - [ ] Each item in sequence is an integer with value between 1 and 6

### Testing - Calculate Score  
- [ ] `test_zilch` - non scoring roll should return 0  
- [ ] `test_ones` - rolls with various number of 1s should return correct score  
- [ ] `test_twos` - rolls with various number of 2s should return correct score  
- [ ] `test_threes` - rolls with various number of 3s should return correct score  
- [ ] `test_fours` - rolls with various number of 4s should return correct score  
- [ ] `test_fives` - rolls with various number of 5s should return correct score  
- [ ] `test_sixes` - rolls with various number of 6s should return correct score  
- [ ] `test_straight` - 1,2,3,4,5,6 should return correct score  
- [ ] `test_three_pairs` - 3 pairs should return correct score  
- [ ] `test_two_trios` - 2 sets of 3 should return correct score  
- [ ] `test_leftover_ones` - 1s not used in set of 3 (or greater) should return correct score  
- [ ] `test_leftover_fives` - 5s not used in set of 3 (or greater) should return correct score  

### Testing - Banker  
- [ ] `bank` method  
    - [ ] should properly add unbanked points to total and return the <b>deposited</b> amount.  
- [ ] `shelf` method  
  - [ ] should properly track unbanked points  
- [ ] `clear_shelf` method  
  - [ ] should remove any unbanked points, resetting to 0  
  - [ ] should not affect previously <b>banked</b> points.  

## Dependencies  
- poetry  
- python  
- pyenv  

## Authors  / Collaborators
- Software Developer: Corey Marchand  
  - [Official Github](https://github.com/corey-marchand)  
- Software Developer: Haley Griffin  
  - [Official Github](https://github.com/h-griffin)  
- Software Developer: Joseph Lee  
  - [Official Github](https://github.com/josephlee3454)  
- Software Developer: Joseph Zabaleta
  - [Official Github](https://github.com/joseph-zabaleta)  

## License  
This project is under the MIT License.

## Acknowledgements / Resources  
- Review [rules of the game](https://en.wikipedia.org/wiki/Dice_10000)  
- Play game [online](http://www.playonlinedicegames.com/farkle)  

## Version History  
- 1.0.0 20200518 0900
    - Initial file structure built.  

