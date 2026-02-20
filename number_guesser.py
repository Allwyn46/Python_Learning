import random

top_of_range = input("Enter a number ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please Enter a number greater than 0")
        quit()
else:
    print("please enter a number")
    quit()

random_number = random.randint(0,top_of_range)
guess = 0;

while True:
    user_guess = input("Make a guess ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please enter a number")
        continue

    if user_guess == random_number:
        print("You got it!")
        print("You took " + str(guess) + " guesses")
        break
    else:
        if user_guess > random_number:
            print("You guessed above the number")
        else:
            print("You guessed below the number")
        guess += 1
        continue