import json

from scripts.link import link

path = 'card_info\cards.json'
def clearJSON():
    global path
    with open(path, 'w') as f:
        with open('card_info\cardstemplate.json', 'r') as f2:
            json.dump(json.load(f2), f, indent= 4, sort_keys= True)

def displayJSON():
    global path
    with open(path, 'r') as f:
        jsonobj = json.load(f)
        out = ""
        for card in jsonobj["data"]["cards"]:
            out += f"ID: {card} \n"
            out += f"Name: {card.cardName}"
            out += f"Set: {card.set}\n"
            out += f"TCGPlayer Price: {card.tcgPlayer.price.market}"
            out += f"TCGPlayer Link: {link(card.tcgPlayer.price.buyURL)}"
            print(out)
