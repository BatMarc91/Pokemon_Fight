import requests
from data.env import url

def search_pokemon(pokemon_name: str):
    consulta = requests.get(f"{url}/pokemon/{pokemon_name.lower()}")

    if consulta.status_code == 200:
        return True
    
    else:
        return False