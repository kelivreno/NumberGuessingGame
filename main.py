import random

def game():
    x = int(input("What number should the range start at? "))
    y = int(input("What number should the range end at? "))
    num = random.randint(x, y)
    num_guess = 0

    if x > y:
        print("Invalid range")
        return

    while True:
        num_guess += 1
        z = int(input("Guess the number: "))
        if z == num:
            print("Congrats you got it right!")
            print(f'The number is {num}')
            print(f'It took you {num_guess}')
            break
        elif z > num:
            print(f"Incorrect, {z} is too high")
        elif z < num:
            print(f"Incorrect number, {z} is too low")

print("====GUESS THE NUMBER====")
game()