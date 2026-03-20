# Number Guessing Game

Practicing making functions, while loop, if-statements, and using the `random` library. 

- The random library will generate an integer within a range that is set by the difficulty of the game determined by the user
- ```python
  if level == 1:
    # 1. EASY MODE (1-10)
    num = random.randint(1,10)
  elif level ==2:
    # 2. MEDIUM MODE (1-100)
    num = random.randint(1,100)
  elif level == 3:
    # 3. HARD MODE (1-1000)
    num = random.randint(1,1000)
```
- A while loop will be activated and it will compare the input from the user to check if it's too high or too low.
- It will continue to count the number of guesses and has max of 5 guesses per game, and compare until the user gets it right, otherwise a message of thank you and sharing what number it is will be displayed
- It now has a `replay()` function!
- The function will see if the user enters `Y/N`, if they chooses <i>Y</i>, the function `game()` will continue to play, otherwise another thank you will show up

## Opportunities to improve:
- Add a foolproof with try/except
