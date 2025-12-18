import requests
from env import url, marc_team
from pydantic import BaseModel

class Pokemon(BaseModel):
    name: str
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int

# Funció definir stats dels pokemons
def pokemon_stats(pokemon_name: str):
    consulta = requests.get(f"{url}/pokemon/{pokemon_name.lower()}")

    if consulta.status_code == 200:
        # Em guardo a un json tota la información del pokemon
        json_pokemon = consulta.json()

        pokemon = Pokemon(
            name = pokemon_name,
            hp = json_pokemon["stats"][0]["base_stat"],
            attack = json_pokemon["stats"][1]["base_stat"],
            defense = json_pokemon["stats"][2]["base_stat"],
            special_attack = json_pokemon["stats"][3]["base_stat"],
            special_defense = json_pokemon["stats"][4]["base_stat"],
            speed = json_pokemon["stats"][5]["base_stat"],
            )

        # return pokemon
        #return Pokemon(
        #    name = pokemon_name,
        #    hp = json_pokemon["stats"][0]["base_stat"],
        #    attack = json_pokemon["stats"][1]["base_stat"],
        #    defense = json_pokemon["stats"][2]["base_stat"],
        #    special_attack = json_pokemon["stats"][3]["base_stat"],
        #    special_defense = json_pokemon["stats"][4]["base_stat"],
        #    speed = json_pokemon["stats"][5]["base_stat"],
        #    )
    
        return {
            "name" : pokemon_name,
            "hp" : json_pokemon["stats"][0]["base_stat"],
            "attack" : json_pokemon["stats"][1]["base_stat"],
            "defense" : json_pokemon["stats"][2]["base_stat"],
            "special_attack" : json_pokemon["stats"][3]["base_stat"],
            "special_defense" : json_pokemon["stats"][4]["base_stat"],
            "speed" : json_pokemon["stats"][5]["base_stat"],
        }
    
    else:
        return "Error"

#print(pokemon_stats("Umbreon"))