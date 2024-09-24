import random

rock = "3"
paper = "2"
scissors = "4"

user = input("Enter 3 for rock, 2 for paper, or 4 for scissors: ")
computer = random.choice([rock, paper, scissors])

if user == rock:
    if computer == rock:
        print("It's a tie!")
    elif computer == paper:
        print("Computer wins!")
    elif computer == scissors:
        print("You win!")
elif user == paper:
    if computer == rock:
        print("You win!")
    elif computer == paper:
        print("It's a tie!")
    elif computer == scissors:
        print("Computer wins!")
elif user == scissors:
    if computer == rock:
        print("Computer wins!")
    elif computer == paper:
        print("You win!")
    elif computer == scissors:
        print("It's a tie!")
else:
    print("Invalid input!")