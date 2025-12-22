from data.env import marc_beginner, marc_mid, marc_expert
from data.env import team_proves
from components.search_pokemon import search_pokemon
from components.stats import pokemon_stats, initial_stats
from components.pokemon_fight import fight
from models.models import PokemonModel, TeamModel, FightModel
from components.generate_fight import generate_fight
from models.battle import PokemonInBattle 

user_team_name = "Equip de proves"
user_list = team_proves

marc_team = TeamModel(name ="Equip de Marc", pokemons=marc_mid)
user_team = TeamModel(name = user_team_name, pokemons= user_list)

# print("Anem a fer el sorteig.......................")

#print(marc_team.pokemons[0])
#team_two.pokemons[num_two].name

matches = generate_fight(marc_team, user_team) # Aquí obtinc un FightModel

# Ara vindrien els enfrontaments
    # Per cada iteració a la llista de sorteig s'ha de fer el pokemon_fight

for match in matches: # match és un FightModel
    print(f"""Combat número {match.num_fight}:
            --> {match.pokemon_one.name} ({match.pokemon_one.team_name}) VS {match.pokemon_two.name} ({match.pokemon_two.team_name})""")

    # Genero estadístiques inicials per a cada pokemon del combat
        # pokemon_one i pokemon_two son un PokemonModel
    pokemon_one = initial_stats(match.pokemon_one)
    pokemon_two = initial_stats(match.pokemon_two)

    # Per defecte el pokemon que primer atacarà serà el de l'equip pre definit. Així en cas d'empat començarà sempre 
    pokemon_attack = pokemon_one
    pokemon_defense = pokemon_two

    # Calculo qui serà el primer pokemon en atacar
    if pokemon_one.speed_points() < pokemon_two.speed_points():
        pokemon_attack = pokemon_two
        pokemon_defense = pokemon_one

    print(f"""      \n-> El primer pokemon en atacar és {pokemon_attack.name} ({pokemon_attack.team_name}), que te una velocitat de {pokemon_attack.speed_points()}
                        {pokemon_defense.name} ({pokemon_defense.team_name}) haurà de defensar-se, ja que te una velocitat de {pokemon_defense.speed_points()}""")
    
    print(fight(pokemon_one, pokemon_two))


    










