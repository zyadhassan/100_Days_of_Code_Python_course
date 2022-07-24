from art import logo


print(logo)


auction={}
more_players=True
while more_players:
    name=str(input("What is your name? :"))
    bid=int(input("What is your bid? $"))
    auction[name]=bid
    more=input("Are there any other bidders ? Type 'yes' or 'no' ").lower()
    if more=='no':
        more_players=False

max_name=""
max_bid=0
for name in auction:
    if auction[name]>max_bid:
        max_name=name
        max_bid=auction[name]


print(f"The winner is {max_name} with a bid of ${max_bid}")