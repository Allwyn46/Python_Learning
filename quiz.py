print("Welcome to my Quiz Game!")

playing = input("Do you wanna play? ")
score = 0

if playing.lower() != "yes":
    quit()
else:
    print("Finally a worthy oponent")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Better Luck next time")
    quit()


answer1 = input("What is the brain of the computer called? ")
if answer1.lower() == "cpu":
    print("correct!")
    score += 1
else:
    print("Better Luck next time")
    quit()


answer2 = input("What type of memory is temporary and loses data when powered off? ")
if answer2.lower() == "ram":
    print("correct!")
    score += 1
else:
    print("Better Luck next time")
    quit()

answer3 = input("What is your age? ")
if answer3.lower() == 23:
    print("correct")
else:
    print("Better Luck next Time")
    quit()