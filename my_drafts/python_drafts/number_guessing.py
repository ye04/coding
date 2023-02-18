import random

def guess(x):
    random_number = random.randint(1, x)
    user_number = 0
    print(random_number)
    while user_number != random_number:
        user_number = int(input("Guess anynumber between 1 and {0}! " .format(x)))
        if user_number > random_number:
            print("Sorry too high")
        elif user_number < random_number:
            print("Sorry too low")
    
    print("Yay! You correctly guessed the number!")

guess(50)

