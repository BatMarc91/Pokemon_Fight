from data.env import marc_beginner, marc_mid, marc_expert
from components.search_pokemon import search_pokemon
from models.models import PokemonModel, TeamModel, FightModel
from components.generate_fight import generate_fight

marc_team = TeamModel(name="Equip de Marc", pokemons=marc_mid)

def intro():
    print("""
    ===========================================
            P O K É M O N   B A T T L E
    ===========================================
    """)

    # petita pausa

    print("Un nou combat està a punt de començar...")
    print("Dos entrenadors. Sis Pokémon. Un únic vencedor.")

    # pausa curta

    print("""
    El teu rival d'avui és:

        🔥 ENTRENADOR MARC 🔥
    """)

    # pausa

    print("Marc ja té el seu equip preparat:")

    print("""
    -------------------------------------------
    """)

    for pokemon in marc_team:
        print(f"  • {pokemon}")

    print("""
    -------------------------------------------
    """)

    # pausa

    print("Ara és el teu torn.")
    print("Necessites preparar un equip de 6 Pokémon per al combat.")

    print()
    print("👉 Primer, introdueix el nom del teu equip:")

    user_team_name = input("> ")

    print()
    print(f"Quin seran els components de {user_team_name}?")

    i = 1
    while i < 7:
        pokemon = input(f"""
                            *** (Fica una X si vols tancar)
                    Pokemon nº {i} -->  
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

    return user_team