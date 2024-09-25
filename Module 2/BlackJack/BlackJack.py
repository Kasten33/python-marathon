import random
import time

deck = {
    "A": [1, 11],
    "2": 2, 
    "3": 3, 
    "4": 4, 
    "5": 5, 
    "6": 6, 
    "7": 7,
    "8": 8, 
    "9": 9,
    "10": 10, 
    "J": 10, 
    "Q": 10, 
    "K": 10
}

def calculateHand(hand):
    value = 0
    aces = 0
    for card in hand:
        if isinstance(card, tuple):
            value += card[1]
        elif card == "A":
            aces += 1
        else:
            value += deck[card]
    for _ in range(aces):
        if value + 11 <= 21:
            value += 11
        else:
            value += 1
    return value

def promptAceValue():
    while True:
        ace_value = input("You drew an Ace! Do you want it to be 1 or 11? ")
        if ace_value == "1":
            return 1
        elif ace_value == "11":
            return 11
        else:
            print("Invalid input. Please enter 1 or 11.")

def drawCard(hand, is_player=True):
    card = random.choice(list(deck.keys()))
    hand.append(card)
    if is_player:
        print(f"You drew a {card}")
    if card == "A" and is_player:
        ace_value = promptAceValue()
        hand[-1] = (card, ace_value)  # Store the chosen value for the Ace separately
    elif card == "A" and not is_player:
        if calculateHand(hand) + 11 - deck["A"][0] <= 21:  # Adjust for the initial Ace value
            hand[-1] = (card, 11)  # Use Ace as 11 if it doesn't make the dealer go bust
        else:
            hand[-1] = (card, 1)   # Otherwise, use Ace as 1
    return card

question = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

if question == "n":
    print("Goodbye!")
    quit()

if question == "y":
    time.sleep(1)
    print("Alright, Let's play!")
    player = []
    dealer = []
    
    # Draw initial cards for player
    for i in range(2):
        drawCard(player)
    print(f"Your cards: {player}, current score: {calculateHand(player)}")
    
    # Draw initial cards for dealer
    for i in range(2):
        drawCard(dealer, is_player=False)
    print(f"Dealer's first card: {dealer[0]}")
    
    while calculateHand(player) < 21:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if another_card == "y":
            time.sleep(1)
            drawCard(player)
            print(f"Your cards: {player}, current score: {calculateHand(player)}")
        if another_card == "n":
            break

    if calculateHand(player) > 21:
        print(f"Your cards: {player}, current score: {calculateHand(player)}")
        print(f"Dealer's final hand: {dealer}, final score: {calculateHand(dealer)}")
        print("You went over 21! You lose.")
        quit()

    if calculateHand(player) == 21:
        print(f"Your final hand: {player}, final score: {calculateHand(player)}")
        print(f"Dealer's final hand: {dealer}, final score: {calculateHand(dealer)}")
        print("You win!")
        quit()
# Dealer's turn: draw cards until the dealer's hand value is at least 17
    while calculateHand(dealer) <= 17:
        drawCard(dealer, is_player=False)

    if calculateHand(dealer) > 21:
        print(f"Dealer's final hand: {dealer}, final score: {calculateHand(dealer)}")
        print("Dealer went over 21! You win.")
        quit()

      
    # Compare final scores to determine the winner
    if calculateHand(player) > calculateHand(dealer):
        print(f"Your final hand: {player}, final score: {calculateHand(player)}")
        print(f"Dealer's final hand: {dealer}, final score: {calculateHand(dealer)}")
        print("You win!")
    elif calculateHand(player) == calculateHand(dealer):
        print(f"Your final hand: {player}, final score: {calculateHand(player)}")
        print(f"Dealer's final hand: {dealer}, final score: {calculateHand(dealer)}")
        print("It's a tie!")
    else:
        print(f"Your final hand: {player}, final score: {calculateHand(player)}")
        print(f"Dealer's final hand: {dealer}, final score: {calculateHand(dealer)}")
        print("Dealer wins.")