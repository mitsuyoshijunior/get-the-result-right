# Math Challenge Game

## Project Overview

This is a simple command-line math game developed in Python. The player chooses a difficulty level and solves randomly generated arithmetic problems (addition, subtraction, multiplication) accordingly. The game tracks the player's score and offers the option to continue playing or exit.

## Features

- Five difficulty levels affecting the range of numbers used  
- Randomly selects operations: addition, subtraction, or multiplication  
- Validates player answers with immediate feedback  
- Tracks the player's score during the session  
- Allows continuous play until the player chooses to quit  

## How to Use

1. Run the main script.  
2. Choose a difficulty level (1 to 4, from easiest to hardest).  
3. Solve the displayed math problem by typing your answer.  
4. Receive feedback and your current score.  
5. Decide whether to continue playing or exit the game.

## Technologies Used

- Python 3.x  

## Project Structure

- `models/calculate.py`: Contains the `Calculate` class, responsible for generating math problems and checking answers.  
- `main.py`: Contains the game loop and user interaction logic.

## Example Output

```
What level of difficulty do you want? Type 1, 2, 3, or 4 — from easiest to hardest.
1
7 + 3 = ?
Type your answer: 10
You are right!
7 + 3 = 10
Congratulations! Your answer is correct! You have 1 points!
Do you want to keep playing? Type 1 for yes or 0 for no.
0
You finished this game with 1 points! See you!
```

## How to Run

Run the script from the command line:

```bash
python main.py
```

## Author

Mitsuyoshi Nakamura Junior
