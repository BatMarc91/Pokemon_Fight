from env import marc_team, team_proves
from stats import pokemon_stats
from search_pokemon import search_pokemon

def get_team_stats(team: list):
    """Retornar json amb l'equip"""
    pokemon_team = {}

    for pokemon in team:
        pokemon_team[pokemon] = pokemon_stats(pokemon)
    
    return pokemon_team
        

#print(get_team(marc_team))
#print(get_team(team_proves))

def select_team():
    """FUnció que genera un equip de 6 pokemon i les seues estadístiques"""
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

