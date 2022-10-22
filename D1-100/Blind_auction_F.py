from art import logo_bid
import os
clear = lambda: os.system('cls')

bidding = {}

def high_bid(bid_reccord):
    highest_bid = 0
    winner = ""
    for bidder in bid_reccord:
        bit_amount = bid_reccord[bidder]
        if bit_amount > highest_bid:
            highest_bid = bit_amount
        winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


game_continue = True

while game_continue:
    print(logo_bid)
    user = input("What's your name? ")
    bid = int(input("What's your bid? $"))
    bidding[user] = bid
    more_bidder = input("Are there any other bidders? Type 'Yes' or 'No' ").lower()
    if more_bidder == "no":
        game_continue = False
        high_bid(bidding)
    else:
        clear()

