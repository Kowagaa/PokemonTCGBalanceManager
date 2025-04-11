import json
import os
import dotenv

from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype
from pokemontcgsdk import Rarity
from pokemontcgsdk import RestClient

dotenv.load_dotenv()

decoder = json.JSONDecoder()

RestClient.api_key = os.environ.get("POKEMON_API_KEY")

def fetchCard(query : str, is_holo : int =0):
    """
    Fetches card from PokemonTCG SDK with query
    is_holo:
    0 - non holo
    1 - holo
    2 - reverse holo
    """
    global decoder
    holo = ["normal", "holofoil", "reverseHolofoil"][is_holo]
    with open('card_info\cards.json', 'r+') as f:
        jsonobj = json.load(f)
        cards = Card.where(q=query)
        for card in cards:
            try:
                eval(f"card.tcgplayer.prices.{holo}.low")
                eval(f"card.tcgplayer.prices.{holo}.mid")
                eval(f"card.tcgplayer.prices.{holo}.high")
                eval(f"card.tcgplayer.prices.{holo}.market")
                card.cardmarket.prices.averageSellPrice
            except:
                print("WARNING: price not available on either TCGPlayer or CardMarket for card", card.name, holo, "with id", card.id, ", check if card exists")
            else:
                jsonobj["data"]["cards"][card.id] = {
                    "cardName" : card.name,
                    "type" : card.types,
                    "set" : {
                        "name" : card.set.name,
                        "total" : card.set.total,
                        "thisNum" : card.number
                    },
                    "tcgPlayer" : {
                        "price" : {
                            "low" : eval(f"card.tcgplayer.prices.{holo}.low"),
                            "mid" : eval(f"card.tcgplayer.prices.{holo}.mid"),
                            "high" : eval(f"card.tcgplayer.prices.{holo}.high"),
                            "market" : eval(f"card.tcgplayer.prices.{holo}.market")
                        },
                        "lastUpdate" : card.tcgplayer.updatedAt,
                        "buyURL" : card.tcgplayer.url
                    },
                    "cardMarket"  :{
                        "price" : [
                            {
                                "avg" : card.cardmarket.prices.averageSellPrice,
                                "low" : card.cardmarket.prices.lowPrice,
                                "suggested" : card.cardmarket.prices.suggestedPrice 
                            },
                            {
                                "avg" : card.cardmarket.prices.reverseHoloSell,
                                "low" : card.cardmarket.prices.reverseHoloLow
                            },
                            {}
                        ][is_holo],
                        "lastUpdate" : card.cardmarket.updatedAt,
                        "buyURL" : card.cardmarket.url
                    }
                }
    with open('card_info\cards.json', 'w') as f:
        json.dump(jsonobj, f, indent= 4, sort_keys= True)

