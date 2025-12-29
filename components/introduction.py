import time
from components.texts.manager import get_text
from data.env import marc_beginner, marc_mid, marc_expert
from components.search_pokemon import search_pokemon
from models.models import TeamModel

def intro(language, difficulty):
    """Funció que fa d'introducció al joc, mostrant idioma i difficultat"""

    if difficulty == "beginner":
        marc_team = TeamModel(name="Equip de Marc", pokemons=marc_beginner)

    elif difficulty == "mid":
        marc_team = TeamModel(name="Equip de Marc", pokemons=marc_mid)
    
    else:
        marc_team = TeamModel(name="Equip de Marc", pokemons=marc_expert)

    print(get_text(language, "title"))
    time.sleep(1.5)

    print(get_text(language, "sub_title")[0])
    time.sleep(1)

    print(get_text(language,"sub_title")[1])
    time.sleep(1)

    print(get_text(language,"sub_title")[2])
    time.sleep(1.5)

    print(get_text(language, "champion_presentation"))
    time.sleep(2)   

    print(get_text(language, "champion_team"))
    time.sleep(1)

    print("""
-------------------------------------------
""")
    time.sleep(0.5)

    for pokemon in marc_team.pokemons:
        print(f"  🔴 {pokemon}")
        time.sleep(0.4)

    time.sleep(0.5)
    print("""
-------------------------------------------
""")
    time.sleep(1.5)

    print(get_text(language, "user_presentation")[0])
    time.sleep(1)

    print(get_text(language, "user_presentation")[1])
    time.sleep(1.5)

    print(get_text(language, "user_presentation")[2])
    time.sleep(0.5)

    user_team_name = input("> ")

    time.sleep(1)
    print(get_text(language, "user_presentation")[3])
    time.sleep(1)

    user_list = []
    i = 1

    while i < 7:
        pokemon = input(f"""
                🧢 Pokémon nº {i}
                    > """)

        if pokemon.upper() == "X":
            print(get_text(language, "game_cancelled"))
            time.sleep(1)
            exit()

        pokemon_found = search_pokemon(pokemon)

        if not pokemon_found:
            print(get_text(language, "text_not_found"))
            time.sleep(1)
        else:
            print(f"✅ {pokemon} {get_text(language, "text_found")}")
            time.sleep(0.5)
            user_list.append(pokemon)
            i += 1

    print(f"{get_text(language, "team_selected")} {user_team_name}")
    time.sleep(1)

    time.sleep(1.5)
    print(get_text(language, "teams_prepared"))
    time.sleep(1)

    user_team = TeamModel(name=user_team_name, pokemons=user_list)

    return [marc_team, user_team]