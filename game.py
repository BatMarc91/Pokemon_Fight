from data.env import marc_beginner, marc_mid, marc_expert
from components.search_pokemon import search_pokemon
from models.models import PokemonModel, TeamModel, FightModel
from components.generate_fight import generate_fight


marc_team = TeamModel(name="Equip de Marc", pokemons=marc_mid)

print(f"""
Benvingut al joc de combats de Pokemon. 
    Avui desafiaràs a Marc i el seu equip Pokemon:
        - {marc_team}
""")


print("Tria un nom per al teu equip de 6 Pokemon")
user_team_name = input("")

i = 1
user_list = []

while i < 7:
    pokemon = input(f"""
                            *** (Fica una X si vols tancar)
                    Ara tria el Pokemon nº {i} -->  
                    """)

    if pokemon == "X":
        exit()
    
    # Comprovar si el pokemon existeix per ficar-lo a l'equip corresponent
    pokemon_found = search_pokemon(pokemon)

    if not pokemon_found:
        "No has escrit bé el pokemon, torna a intentar-ho."
    
    else:
        i = i + 1 # seguir avançant amb el bucle

        # Afegir cada pokemon a la llista de l'equip
        user_list.append(pokemon)

user_team = TeamModel(name = user_team_name, pokemons= user_list)

print(f"Genial, aquí tens el teu equip: {user_team}")

print("Anem a fer el sorteig.......................")

sorteig = generate_fight(marc_team, user_team)

print(sorteig)








