print("Welcome to the secret auction program.")
def win_bid(overall_bids):
    highest_bid = 0
    Kit = ''
    for bids in overall_bids:
        value = overall_bids[bids]
        if value > highest_bid:
            highest_bid = value
            Kit = bids
    print(f"The winner is {Kit} with a bid of ${highest_bid}.")
overall_bids = {}
on = True
while on == True:
    name = (input("What is your name?: \n")).title()
    bid = int(input("What's your bid?: \n$ "))
    overall_bids[name] = bid
    other_bidders = (input("Are there any other bidders? Type 'yes' or 'no'. \n")).lower()
    if other_bidders == 'no':
        on = False
        win_bid(overall_bids)
    print(overall_bids)
    print("*********************************\n****************************")
    
