import random
import time
word_list = ["aardvark", "baboon", "camel", "dolphin", "elephant", "flamingo",
              "giraffe", "hippopotamus", "iguana", "jaguar", "kangaroo", "llama", "monkey", 
              "narwhal", "orangutan", "penguin", "quokka", "rhinoceros", "squirrel", "tiger", 
              "umbrellabird", "vulture", "walrus", "xerus", "yak", "zebra", "cat", "dog", "bird",]
player_lives = "|"
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
max_lives = 5
current_lives = max_lives

display = ["-"] * word_length

print("Welcome to Hangman!")
start = input("Do you want to play Hangman? Type 'yes' or 'no': ").lower()

if start == "no":
  print("Goodbye!")
  exit()
else:
  print("Let's play Hangman!")
  print("I'm thinking of a word.")
time.sleep(2)

print(f'The word has {word_length} letters.')
print(f'You have {player_lives * current_lives} Lives')
print(" ".join(display))

while current_lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        print(f"Good guess! The letter '{guess}' is in the word.")
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
    else:
        current_lives -= 1
        print(f"Sorry, the letter '{guess}' is not in the word.")
    
    print(f'You have {player_lives * current_lives} Lives')
    print(" ".join(display))

    if current_lives == 0:
        print("You've run out of lives! Game over.")
        break

    if "-" not in display:
        print("Congratulations! You've guessed the word!")
        break
  





