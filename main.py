import random

def game():
    print("1. EASY: 1-10")
    print("2. MEDIUM: 1-100")
    print("3. HARD: 1-1000")
    level = int(input("Which mode would you like? (enter the number): "))

    if level == 1:
        num = random.randint(1,10)
    elif level == 2:
        num = random.randint(1,100)
    elif level == 3:
        num = random.randint(1,1000)


    # x = int(input("What number should the range start at? "))
    # y = int(input("What number should the range end at? "))
    # num = random.randint(x, y)
    num_guess = 0
    #
    # if x > y:
    #     print("Invalid range")
    #     return

    while True:
        num_guess += 1
        if num_guess <= 5:
            z = int(input("Guess the number: "))
            if z == num:
                print("Congrats you got it right!")
                print(f'The number is {num}')
                print(f'It took you {num_guess} guesses')
                break
            elif z > num:
                print(f"Incorrect, {z} is too high")
            elif z < num:
                print(f"Incorrect number, {z} is too low")
        else:
            print(f"Thank you for playing, the number is {num}")
            break

def replay():
    p = input("Would you like to play again? (Y/N) ")
    ans = p.lower()
    if ans == 'y':
        game()
    if ans == 'n':
        print('Thank you for playing')

print("====GUESS THE NUMBER====")
game()
replay()