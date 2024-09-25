import data
import random
import time

def game():
    score = 0
    game_over = False
    while not game_over:
        account_a = random.choice(data.data)
        account_b = random.choice(data.data)
        while account_a == account_b:
            account_b = random.choice(data.data)
        print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
        print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if account_a['follower_count'] > account_b['follower_count']:
            correct_answer = 'a'
        else:
            correct_answer = 'b'
        if guess == correct_answer:
            score += 1
            print(f"Correct! Your current score is {score}.")
        else:
            print(f"Sorry, that's wrong. Your final score is {score}.")
            game_over = True

#console stuff, functionality

print("Hello, welcome to the Higher Lower Game!")
Start = input("Do you want to play? Type 'yes' or 'no': ").lower()
if Start == "no":
    print("Goodbye!")
    quit()
if Start == "yes":
    print("Alright, let's play!")
    time.sleep(1)
    game()

