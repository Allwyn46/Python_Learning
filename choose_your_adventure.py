name = input("Enter your name: ")
print("Welcome to grand line", name)

answer = input("you entered grand line, after entering grand line your compass is not working. now you have two options wander on your own in the open sea? or stay with laboon for a Day? Enter 1 for wander on the sea or Enter 2 for staying with laboon: ").lower()

if answer == "1":
    print("You chose to wander on the open sea and you got lost")
    quit()
elif answer == "2":
    answer = input("You stayed with laboon and found out that a old man crocs is living inside laboon he told you about the log pose and gave one tou you. You also found two people inside mrs.wednesday and his partner they say they know about the island the log pose is pointing and they are asking you to take them there. Enter 1 to take them, Enter 2 to leave them in the middle of the ocean: ")

    if answer == "1":
        answer = input("You took them to the island. the island is called whisky peak. They are so generous to you and your crew. they gave you food and accomadation for free. later your crewmate find out that all the people the in the island are assains from a organization called baraque works. they try to kill your crewmate but they are no match for him. ")
else:
    print("Choose a valid option! ")