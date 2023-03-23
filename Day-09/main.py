from replit import clear
from art import logo

print(logo)
print("Welcome secret auction program .")
bids = {}

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
while_continue = True
while while_continue:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  
  bids[name] = price
  
  new_bidder = input("Are there any other bidders? Type 'yes or 'no'. \n").lower()
  if new_bidder == "yes":
    clear()
  elif new_bidder == "no":
    while_continue = False
    find_highest_bidder(bids)
