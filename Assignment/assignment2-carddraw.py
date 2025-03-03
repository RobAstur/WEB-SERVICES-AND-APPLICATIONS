import requests

# Shuffle the deck
shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(shuffle_url)

# if the request is succesful, proceed with the 5 cards
if response.status_code == 200:
    deck_id = response.json()["deck_id"]

    # Draw 5 cards from the shuffled deck
    draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
    response = requests.get(draw_url)

    if response.status_code == 200:
        cards = response.json()["cards"]
        
        # Loop the cards. print card value and suit 
        for card in cards:
            print(f"Card: {card['value']} of {card['suit']}")
    else:
        print("Error drawing cards.")
else:
    print("Error shuffling deck.")
