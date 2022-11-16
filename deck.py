
from webbrowser import get
import requests

class Deck():
    url =  'https://www.deckofcardsapi.com/api/deck/2tttz40fqdio/'
    deck_id = 'z0m0j5le7c56'
    response = requests.post(url)
    deck = response.json()
    cards_left = int(deck['remaining'])
    cards = deck 

    def get_card(self):
        card_draw = requests.get('https://www.deckofcardsapi.com/api/deck/2tttz40fqdio/draw/?count=1')
        card = card_draw.json()
        revised_card = {
            'value': card['cards'][0]['value'],
            'suit': card['cards'][0]['suit'],
            'image': f"{card['cards'][0]['code']}"
        }
        if revised_card['value'].isdigit():
            revised_card['points'] = int(revised_card['value'])
        elif revised_card['value'] == 'ACE':
            revised_card['points'] = 11
        else:
            revised_card['points'] = 10
        return revised_card

    
    def shuffle(self):
        data = 'https://www.deckofcardsapi.com/api/deck/2tttz40fqdio/shuffle/'
        reshuffle = requests.post(data)
        return reshuffle.json()







