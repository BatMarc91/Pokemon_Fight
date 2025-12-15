from env import marc_team, team_proves
from pokemon_stats import pokemon_stats, show_team
from pkmn_fight import combat_selection, fight
from datetime import datetime
import time

# Aquí faré tot joc

# Text d'introducció al joc
print(""" Avui tindràs l'honor d'enfrontar-te a BatMarc en un combat Pokemon!
    Primer esculliràs 6 Pokemons per al teu equip. Estos s'enfrontaran en combats 
    individuals a un dels Pokemons de Marc.""")

# El jugador tria el seu nom i el seu equip pokemon
"""
player_name = input("Quin serà el nom del teu equip? ")
i = 1
player_team = []
while i < 7:
    pokemon = input(print(f"Escull el Pokemon nº {i}: "))
    player_team.append(pokemon)
    i = i + 1
"""
player_name = "Equip de proves"
player_team = team_proves

# Mostro l'equip del jugador
print("Una vegada triat el teu equip, anem a mostrar les seues estadístiques")
player = pokemon_stats(player_name, player_team)
show_team(player_name,player)
#time.sleep(2)

# Mostro l'equip de Marc
print("Vols saber a qui t'hauràs d'enfrontar?")
marc = pokemon_stats("Els destructors de somnis", marc_team)
show_team("Els destructors de somnis",marc)

# Fem el sorteig i mostrem els combats
print("Ara que ja coneixem als dos equips, nem a veure els 6 enfrentaments que tindrem:")
combats = combat_selection(player, marc)
print(combats)
# combats -> list
#data = [
#    'Combat 5',
#    {2: {'name': 'Typhlosion', 'type': 'Fire', 'stats': {'hp': 78, 'attack': 84, 'defense': 78, 'special-attack': 109, 'special-defense': 85, 'speed': 100}}},
#    {1: {'name': 'Zapdos', 'type': 'Electric', 'stats': {'hp': 90, 'attack': 90, 'defense': 85, 'special-attack': 125, 'special-defense': 90, 'speed': 100}}}
#]
for combat in combats:
    print(combat[1])
    #for name in combat[1].values():
    #    print(f"El combat nº {combat[0]} serà entre {name["name"]} i {name["name"]}.")

# Aquí farem els combats
#fight(combats)
