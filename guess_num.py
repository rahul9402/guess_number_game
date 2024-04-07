import random

random_number = random.randint(1,100)

def guess():
    lives = 0
    level = input("Choose level of difficulty 'easy' or 'hard' ").lower()

    if level == "easy":
        lives = 10
    else:
        lives = 5

    flag = True
    while flag:

        print(f"You have {lives} attempts to guess a number")
        guessed_number = int(input("Make a guess: "))

        if guessed_number < random_number:
            lives-=1
            if lives!=0:
                print("Your guess is too low")
                print("Guess again")
            else:
                flag = False
                print("Your guess is too low")
                print(f"You Lose... Correct Number is {random_number}")
        elif guessed_number > random_number:
            lives-=1
            if lives!=0:
                print("Your guess is too high")
                print("Guess again")
            else:
                flag = False
                print("Your guess is too high")
                print(f"You Lose... Correct Number is {random_number}")
        else:
            flag = False
            print("You have guessed correct number.You Won...")

guess()
