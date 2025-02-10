import requests
from xml.dom import minidom

# Shuffle the deck and get deck_id (XML response)
response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
doc = minidom.parseString(response.text)
print(doc.toprettyxml(), end = "")