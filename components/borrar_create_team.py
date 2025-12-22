import random

from data.env import marc_team, team_proves
from stats import pokemon_stats
from search_pokemon import search_pokemon

def create_team():
    """Funció que genera un equip de 6 pokemon i les seues estadístiques"""
    i = 1
    team_list = []

    while i < 7:
        pokemon = input(f"Escull el Pokemon nº {i}: ")

        pokemon_found = search_pokemon(pokemon)

        if pokemon_found:
            team_list.append(pokemon)
            i = i + 1
        
        else:
            return "Error -> Pokemon no trobat a la base de dades"
    
    team = get_team_stats(team_list)

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

team_one = get_team_stats(marc_team)
team_two = get_team_stats(team_proves)

print(generate_fight(team_one, team_two))

