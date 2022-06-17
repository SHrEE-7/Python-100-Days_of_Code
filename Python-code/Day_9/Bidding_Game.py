import os
print('''            __
               (_()  \
          \__/  ||    \  \__/
          (oo)  /)       (oo)
         //~~\\//       //~~\\
         \\__/\/   _____\\__//_____
          |/\|    |                |
    _____ |||| ___|                |______
   ______(_)(_)___|________________|____
''')

bids = {}
bidding_finished = False
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with the bid amount ₹{highest_bid}")

while not bidding_finished:
  name = input("what is your name?\n")
  price = int(input("What is your bid? ₹"))
  bids[name]=price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'\n")
  if should_continue == 'no':
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue =='yes':
    os.system('cls')
