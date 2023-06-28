```python
class AuctionItem:
    def __init__(self, name, picture, start_price):
        self.name = name
        self.picture = picture
        self.start_price = start_price
        self.highest_bidder = None
        self.highest_bid = 0

    def update_bid(self, bidder, bid_amount):
        if bid_amount >= self.start_price and bid_amount > self.highest_bid:
            self.highest_bidder = bidder
            self.highest_bid = bid_amount


def auctioneer(items):
    print("Welcome to the Auctioneer Program!")
    print("-------------------------------")

    bidders = {}
    for item in items:
        bidders[item.name] = []

    while True:
        print("\nAvailable items for bidding:")
        for item in items:
            print(f"{item.name} - Picture: {item.picture} (Start Price: {item.start_price})")

        print("\nPlease select an item to bid on (or enter 'q' to quit):")
        item_name = input()

        if item_name == 'q':
            break

        if item_name not in bidders:
            print("Invalid item selection. Please try again.")
            continue

        print(f"\nBidding for item: {item_name}")
        bidder_name = input("Enter your name: ")
        bid_amount = int(input("Enter your bid amount: "))

        if bidder_name in bidders[item_name]:
            print("You have already bid on this item. Please try again.")
            continue

        if bid_amount < items[item_name].start_price:
            print("Bid amount is below the starting price. Please try again.")
            continue

        bidders[item_name].append(bidder_name)
        items[item_name].update_bid(bidder_name, bid_amount)

    print("\nAuction Results:")
    for item in items:
        print(f"\nItem: {item.name}")
        if item.highest_bidder:
            print(f"Highest Bidder: {item.highest_bidder}")
            print(f"Highest Bid: {item.highest_bid}")
        else:
            print("No bids received for this item.")

    print("\nThank you for participating in the auction!")
