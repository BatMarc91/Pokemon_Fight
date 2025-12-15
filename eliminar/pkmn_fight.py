from variables_entorn import marc_team
from pokemon_stats import pokemon_stats
import random

def combat_selection(player_team, marc_team):
    player_list = [0, 1, 2, 3, 4, 5]
    marc_list = [0, 1, 2, 3, 4, 5]
    sorteig = []

    for number in range (1,7):
        # Trio número de Pokemon del jugador
        numero = random.choice(player_list)
        player_pokemon = player_team[numero]
        player_list.remove(numero) # borrar el número de la llista per no tornar-lo a repetir
        
        # Trio número de Pokemon de Marc
        numero = random.choice(marc_list)
        marc_pokemon = marc_team[numero]
        marc_list.remove(numero) # borrar el número de la llista per no tornar-lo a repetir

        # retorno una llista amb els combats --> [ "combat 1", "marc_pokemon", "player_pokemon"]
        combat = {number}, {marc_pokemon}, {player_pokemon}

        sorteig.append(combat)
        
    return sorteig

def fight(sorteig):
    pass


