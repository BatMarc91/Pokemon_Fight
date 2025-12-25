from models.models import PokemonModel
from models.battle import PokemonInBattle
from components.stats import initial_stats

def choose_first_attack(pokemon_one: PokemonModel, pokemon_two: PokemonModel):
    pokemon_one_battle = initial_stats(pokemon_one)
    pokemon_two_battle = initial_stats(pokemon_two)

    if pokemon_one_battle.speed_points() > pokemon_two_battle.speed_points():
        return True
    
    else:
        return False

def fight(pokemon_one: PokemonModel, pokemon_two: PokemonModel, pokemon_one_attack=True):
    """Funció que simula tot el combat i retorna el guanyador juntament amb el seu HP actual"""

    if pokemon_one_attack:
        attack_damage  = pokemon_one.physic_damage()
        defense_damage = pokemon_two.defense_damage()

        damage = attack_damage - defense_damage

        if damage > 0:
            # Si l'atac és positiu significa que s'ha superat la defensa, per tant, restem HP
                # pokemon defense ha de restar hp - attack_damage
            damage_received = pokemon_defense.hp - damage
            pokemon_two.hp = damage_received

    return f"Retorno els valors del pokemon atacat {pokemon_two_battle.hp} / {pokemon_one_battle.hp}  --> {pokemon_defense.hp}"
