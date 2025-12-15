import requests

from variables_entorn import url, marc_team

# Necessito tenir els stats de cada un d'ells:
    # Vida
    # Punts atac i especial
    # Punts defensa i especial
    # Velocitat
    # Tipo

# Funció definir stats dels pokemons
def pokemon_stats(team_name:str, pokemon_team: list, url=url) -> list: # retornaré una llista d'este estil ["pokemon_1": {"name" : "name","type" : "type", "stats" : {"HP" : "hp","attack" : "attack","deffence" : "deffence","speed" : "speed"}}, "pokemon_2": .....]
    numero = 0
    your_team = []

    for pokemon in pokemon_team:
        numero = numero + 1
        
        consulta = requests.get(f"{url}/pokemon/{pokemon.lower()}")

        if consulta.status_code == 200:
            # Em guardo a un json tota la información del pokemon
            json_pokemon = consulta.json()

            # Obtenir nom
            name = json_pokemon["forms"][0]
            pokemon_name = name["name"]

            # Obtenir tipus
            type = json_pokemon["types"][0]
            type = type["type"] 
            pokemon_type = type["name"]

            # Obtenir stats --> Aquí el que vull es consultar el json i obtenir els stats que estan a una llista de diccionaris
            stats = {}
            for stat in json_pokemon["stats"]:
                #print(stat["stat"]["name"])
                estado = stat["stat"]["name"]
                stats[estado] = stat["base_stat"]

            your_team.append({numero : { "name" : pokemon_name.capitalize(), "type" : pokemon_type.capitalize(), "stats" : stats}})

        else:
            print(f"Error {consulta.status_code} en la consulta a la {url}")

    return your_team

def show_team(name, team):
    #print("El teu equip Pokemon:") 
    print(f"{name}")
    for i, pokemon in enumerate(team, start = 1):
        name = pokemon[i]["name"]
        tipo = pokemon[i]["type"]
        stats = pokemon[i]["stats"]
        points = f"""VIDA: {stats["hp"]}
                    ATAC: {stats["attack"]}
                    AT. ESPECIAL: {stats["special-attack"]}
                    DEFENSA: {stats["defense"]}
                    DEF. ESPECIAL: {stats["special-defense"]}
                    VELOCITAT: {stats["speed"]}"""

        print(f"""    * {i}.{name} ({tipo})
                    {points}""")