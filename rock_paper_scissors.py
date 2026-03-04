import random

user_score = 0
computer_score = 0
draw_score = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Enter Rock/ Paper/ Scissor  or Q to Quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0,2)

    #rock:0, paper:1, scissors:2

    computer_pick = options[random_number]
    print("Computer picked", computer_pick)

    if user_input == "rock" and computer_pick == "scissors":
        print("Computer picked", computer_pick)
        print("You won")
        user_score += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("Computer picked", computer_pick)
        print("You won")
        user_score += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("Computer picked", computer_pick)
        print("You won")
        user_score += 1
    elif user_input == "rock" and computer_pick == "rock":
        print("Computer picked", computer_pick)
        print("Its a draw")
        draw_score += 1
    elif user_input == "paper" and computer_pick == "paper":
        print("Computer picked", computer_pick)
        print("Its a draw")
        draw_score += 1
    elif user_input == "scissors" and computer_pick == "scissors":
        print("Computer picked", computer_pick)
        print("Its a draw")
        draw_score += 1
    else:
        print("Computer won")
        computer_score += 1
    
    
print("you won", user_score, "times")
print("computer won", computer_score, "times")
print("Total Draws", draw_score)
print("Thank you for playing")