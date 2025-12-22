import random
from models.models import PokemonModel, TeamModel, FightModel

# Genero el sorteig amb les classes creades
def generate_fight(team_one: TeamModel, team_two: TeamModel):
    """Funció que retorna una llista de FightsModels amb els enfrontaments del combat"""
    positions_one = ["0","1", "2", "3", "4", "5"]
    random.shuffle(positions_one)

    positions_two = ["0", "1", "2", "3", "4", "5"]
    random.shuffle(positions_two)

    num_fight: int = 1
    position = 0
    fights = []

    while position < 6:

        num_one = int(positions_one[position])
        num_two = int(positions_two[position])

        pokemon_one = team_one.pokemons[num_one]
        pokemon_two = team_one.pokemons[num_two]

        # Això hauria de ser un FightModel
        fight = FightModel(
            num_fight=num_fight, 
            
            pokemon_one= PokemonModel(
                team_name=team_one.name, 
                name=pokemon_one
                ), 

            pokemon_two=PokemonModel(
                team_name=team_two.name, 
                name=pokemon_two
                )
            )
        
        fights.append(fight)
        
        position = position + 1
        num_fight = num_fight + 1

        #fights[f"fight{num_fight}"] = {
        #            "pokemon_one" : team_one.pokemons[num_one],
        #            "pokemon_two" : team_two.pokemons[num_two]
        #            }
    
    # Això hauria de ser una llista de FightModel
    return fights

