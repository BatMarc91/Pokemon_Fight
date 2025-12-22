from models.models import PokemonModel
from models.battle import PokemonInBattle
from components.stats import initial_stats

def fight(pokemon_one: PokemonModel, pokemon_two: PokemonModel):
    """Funció que simula tot el combat i retorna el guanyador juntament amb el seu HP actual"""

    pokemon_one_battle = initial_stats(pokemon_one)
    pokemon_two_battle = initial_stats(pokemon_two)

    # Calculo qui serà el primer pokemon en atacar
    pokemon_attack = pokemon_one_battle
    pokemon_defense = pokemon_two_battle

    if pokemon_attack.speed_points() < pokemon_defense.speed_points():
        pokemon_attack = pokemon_two_battle
        pokemon_defense = pokemon_one_battle

    # Un dels dos pokemons ataca i li resta punts HP a l'altre
    attack_damage = pokemon_attack.physic_damage()
    defense_damage = pokemon_defense.defense_damage()

    damage = attack_damage - defense_damage

    if damage > 0:
        # Si l'atac és positiu significa que s'ha superat la defensa, per tant, restem HP
            # pokemon defense ha de restar hp - attack_damage
        difference_damage_received = pokemon_defense.hp - attack_damage
        pokemon_defense.hp = difference_damage_received

    return f"Retorno els valors del pokemon atacat {pokemon_two_battle.hp} / {pokemon_one_battle.hp}  --> {pokemon_defense.hp}"
