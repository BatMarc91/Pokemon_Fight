import requests
from data.env import url
from models.models import PokemonModel, PokemonStats
from models.battle import PokemonInBattle

# Funció definir stats dels pokemons
def pokemon_stats(team_name: str, pokemon_name: str):
    consulta = requests.get(f"{url}/pokemon/{pokemon_name.lower()}")

    if consulta.status_code == 200:
        # Em guardo a un json tota la información del pokemon
        json_pokemon = consulta.json()

        return PokemonStats(
            team_name = team_name,
            name = pokemon_name,
            hp = json_pokemon["stats"][0]["base_stat"],
            attack = json_pokemon["stats"][1]["base_stat"],
            defense = json_pokemon["stats"][2]["base_stat"],
            special_attack = json_pokemon["stats"][3]["base_stat"],
            special_defense = json_pokemon["stats"][4]["base_stat"],
            speed = json_pokemon["stats"][5]["base_stat"],
            )
        
    else:
        return "Error"


def initial_stats(pokemon: PokemonModel):
    stats_in_battle = pokemon_stats(pokemon.team_name, pokemon.name)

    stats_in_battle = PokemonInBattle(
        team_name=stats_in_battle.team_name,
        name=stats_in_battle.name,
        hp=stats_in_battle.hp,
        attack=stats_in_battle.attack,
        defense=stats_in_battle.defense,
        special_attack=stats_in_battle.special_attack,
        special_defense=stats_in_battle.special_defense,
        speed=stats_in_battle.speed
    )

    return stats_in_battle