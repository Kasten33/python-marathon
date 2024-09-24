import os

print("Welcome to the secret auction program")

class Bidder:
    def __init__(self, name, bid):
        self.name = name
        self.bid = bid

bidders_list = []

while True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    

    bidder = Bidder(name, bid)
    bidders_list.append(bidder)
    
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if more_bidders == 'yes':

        os.system('cls' if os.name == 'nt' else 'clear')
    elif more_bidders == 'no':
        break


highest_bid = 0
winner = None
for bidder in bidders_list:
    if bidder.bid > highest_bid:
        highest_bid = bidder.bid
        winner = bidder

if winner:
    print(f"Congratulations {winner.name}! You won with ${winner.bid} dollars.")