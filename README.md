# Lab: Class 06 - Class 09 Greed Game

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
      - [x] Add a `shelf` instance method  
        - [x] Input to `shelf` is the amount of points(integer) to add to shelf.  
        - [x] `shelf` should temporarily store <b>unbanked</b> points.  
      - [x] Add a `bank` instance method  
        - [x] `bank` should add any points on the <b>shelf</b> to total and reset shelf to 0  
        - [x] `bank` output should be the amount of points added to total from shelf  
      - [x] Add a `clear_shelf` instance method  
        - [x] `clear_shelf` should remove all unbanked points.

### Class 07 Greed Part 2  
- Extend Game of Greed to get the game in a playable state.  
- [x] Application should implement all features from previous version  
- [x] Application should simulate rolling between 1 and 6 dice  
- [x] Application should allow user to set aside dice each roll  
- [x] Application should allow "banking" current score or rolling again  
- [x] Application should keep track of total score  
- [x] Application should keep track of current round  
- [x] Application should have automated tests to ensure proper operation  

### Class 08 Greed Part 3  
- Extend Game of Greed to get the game in a playable state. 
- [x] Should handle when cheating occurs.  
- [x] Should allow user to continue rolling with 6 new dice when all dice have scored in current turn.  
- [x] Handle zilch  
  - No points for the round, and the round is over.  

### Class 09 Greed Part 4 
- Extend Game of Greed to allow AI Bot to play 
  - [x] Create an AI Bot to play Game of Greed 
  - [x] Bot Class should be added to `player_bot.py` file.  
  - [x] User should be able to see your bot play by executing `player_bot.py` from terminal. 

## User Acceptance Tests  
- [x] Convert required features into suite of passing unit tests  
  - Example Given: `test_roll`:  
    - doing a roll with x number of dice should return a sequence of x length random integers between 1 and 6 inclusive.  
- [x] Use an automated tool to ensure correct behavior from end user's perspective.  

### Testing - Roll Dice
- [x] When rolling 1 to 6 dice ensure:
  - [x] A sequence of correct length is returned  
  - [x] Each item in sequence is an integer with value between 1 and 6

### Testing - Calculate Score  
- [x] `test_zilch` - non scoring roll should return 0  
- [x] `test_ones` - rolls with various number of 1s should return correct score  
- [x] `test_twos` - rolls with various number of 2s should return correct score  
- [x] `test_threes` - rolls with various number of 3s should return correct score  
- [x] `test_fours` - rolls with various number of 4s should return correct score  
- [x] `test_fives` - rolls with various number of 5s should return correct score  
- [x] `test_sixes` - rolls with various number of 6s should return correct score  
- [x] `test_straight` - 1,2,3,4,5,6 should return correct score  
- [x] `test_three_pairs` - 3 pairs should return correct score  
- [x] `test_two_trios` - 2 sets of 3 should return correct score  
- [x] `test_leftover_ones` - 1s not used in set of 3 (or greater) should return correct score  
- [x] `test_leftover_fives` - 5s not used in set of 3 (or greater) should return correct score  

### Testing - Banker  
- [x] `bank` method 
    - [x] should properly add *shelved* points to total and return the <b>deposited</b> amount.  
- [x] `shelf` method  
  - [x] should properly track *shelved* points  
- [x] `clear_shelf` method  
  - [x] should remove any *shelved* points, resetting to 0  
  - [x] should not affect previously <b>banked</b> points.  

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
- 1.0.1 20200518 1230  
  - Created a production branch for lab06 work day.  
  - All work done in VScode LiveShare under Griffin's Computer.  
  - Added key features of todays labs
- 1.0.2 20200519 1330  
  - Created lab07 branch for working on next set of features.  
  - Collaborated on VSCode via LiveShare.  
  - Created Game Class 
  - Created methods for game class to make game playable.  
- 1.0.3 20200520 1230  
  - Created lab08 branch for working on next set of features.  
  - Collaborated on VSCode via LiveShare.  
  - Created cheat_fix function  
  - Created hot_dice function  
  - Created Zilch function  
  - All features, unit tests, and automated tests are working.  
- 1.0.4 20200521 1300  
  - Created lab09 branch for working on next set of featuers.  
  - Collaborated on VSCode via LiveShare.  
  - Created player_bot.py  
  - Created a RiskyBob Bot.  
  - No new unit tests implemented.  
