print("Welcome to my Quiz Game!")

playing = input("Do you wanna play? ")

if playing != "yes":
    quit()
else:
    print("Finally a worthy oponent")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("correct!")
else:
    print("Better Luck next time")
    quit()


answer1 = input("What is the brain of the computer called? ")
if answer1 == "cpu":
    print("correct!")
else:
    print("Better Luck next time")
    quit()


answer2 = input("What type of memory is temporary and loses data when powered off? ")
if answer2 == "ram":
    print("correct!")
else:
    print("Better Luck next time")
    quit()

answer3 = input("What is your age? ")
if answer3 == 23:
    print("correct")
else:
    print("Better Luck next Time")
    quit()