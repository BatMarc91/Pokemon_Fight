import random

def generate_fight(team_one: dict, team_two:dict):
    positions_one = ["1", "2", "3", "4", "5", "6"]
    random.shuffle(positions_one)

    positions_two = ["1", "2", "3", "4", "5", "6"]
    random.shuffle(positions_two)

    num_fight = 1
    position = 0
    fights = {}

    while position < 6:

        fights[f"fight{num_fight}"] = {
                    "pokemon_one" : team_one[positions_one[position]]["name"],
                    "pokemon_two" : team_two[positions_two[position]]["name"]
                    }
        
        position = position + 1
        num_fight = num_fight + 1
    
    return fights

