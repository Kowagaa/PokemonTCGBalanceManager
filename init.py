import scripts.tcg_api as tcg_api
import scripts.json_manipulation as json_man
from scripts.link import link
option = ""


print("+---------------------------------------------------+")
print("|      Welcome to Pokemon TCG Balance Manager       |")
print("+---------------------------------------------------+")

while not(option.lower() in ["exit", "leave", "close"]):
    print("\nWhat would you like to do\n")
    print("1) Edit owned cards list")
    print("2) Check card info")
    print("3) Check out my github\n")
    option = input()
    match option:
        case "1":
            option = input("Would you like to add (1) or remove (2) a new card:\n\n")
            match option:
                case "1":
                    query = input(f"Please input the query as stated {link('https://docs.pokemontcg.io/api-reference/cards/search-cards', 'here')} (The API docs): \n\n")
                    is_holo = input("What version of this card do you want [1. non-holo, 2. holo, 3. reverse holo] \n\n")
                    json_man.clearJSON()
                    tcg_api.fetchCard(query)
                    json_man.displayJSON()
                    
                case "2":
                    print("TODO")
        case "2":
            print("TODO")
        case "3":
            print(link('https://github.com/Kowagaa'))