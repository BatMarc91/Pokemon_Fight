from models.models import PokemonModel
from models.battle import PokemonInBattle, BattleResults
from components.stats import initial_stats
from data.formules import choose_first_attack, physical_attack, calculate_points

def log_combat(log, torn, pokemon_one, damage_one,  hp_one, pokemon_two, damage_two, hp_two):
    """Funció que retorna un diccionari amb els atacs, defensa i hp de cada torn"""
    log[torn] = {
                "pokemon_one" : pokemon_one,
                "damage_one": damage_one,
                "hp_one": hp_one, 
                "damage_two": damage_two,
                "pokemon_two" : pokemon_two,
                "hp_two": hp_two
                        }   

def battle(pokemon_one: PokemonModel, pokemon_two: PokemonModel):
    """Funció que rep 2 Pokemon, els transforma a PokemonInBattle i va restant punts HP fins que un quedi a 0 per retornar el guanyador.
    Finalment retorna una llista amb 3 elements [log combats, punts guanyats]
    """

    # Calculo stats de cada Pokemon
    pokemon_one_battle = initial_stats(pokemon_one) # Això ja es un PokemonInBattle
    pokemon_two_battle = initial_stats(pokemon_two) # Això ja es un PokemonInBattle

    # Inicialitzo stats principals per al xombat
    speed_one = pokemon_one_battle.speed_points()
    speed_two = pokemon_two_battle.speed_points()

    initial_hp_one = pokemon_one_battle.hp
    initial_hp_two = pokemon_two_battle.hp
    
    hp_one = pokemon_one_battle.hp
    hp_two = pokemon_two_battle.hp

    attack_one = pokemon_one_battle.physic_damage()
    defense_one = pokemon_one_battle.defense_damage()
    attack_two = pokemon_two_battle.physic_damage()
    defense_two = pokemon_two_battle.defense_damage()

    # Incialitzo torn i log
    torn = 0
    log = {}

    while hp_one > 0 and hp_two > 0: # Es fan atacs fins que un dels HP < 0

        # El pokemon més ràpid té més opcions d'atacar primer, però no sempre serà així
        first_attack = choose_first_attack(speed_one, speed_two)
        
        # El pokemon més ràpid atac i fa mal a l'altre
        #if speed_one > speed_two: # Tot l'actac estarà dins de l'if
        if first_attack == 1: # ataca el pokemon 1, sino ho farà el 2
            damage_one = physical_attack(attack_one, defense_two)
            damage_two = 0

            hp_two = hp_two - damage_one

            torn = torn + 1
            log_combat(log, torn, pokemon_one.name, damage_one, hp_one, pokemon_two.name, damage_two, hp_two)

            if hp_two > 0: # Com ha sobreviscut, passa a atacar
                damage_one = 0
                damage_two = physical_attack(attack_two, defense_one)
                hp_one = hp_one - damage_two

                torn = torn + 1
                log_combat(log, torn, pokemon_two.name, damage_two, hp_two, pokemon_one.name, damage_one, hp_one)
            

        else:
            damage_one = 0
            damage_two = physical_attack(attack_two, defense_one)
            hp_one = hp_one - damage_two

            torn = torn + 1
            log_combat(log, torn, pokemon_two.name, damage_two, hp_two, pokemon_one.name, damage_one, hp_one)

            if hp_one > 0:
                damage_one = physical_attack(attack_one, defense_two)
                damage_two = 0

                hp_two = hp_two - damage_one

                torn = torn + 1
                log_combat(log, torn, pokemon_one.name, damage_one, hp_one, pokemon_two.name, damage_two, hp_two)

        # Actualitzo els HP de cada pokemon després que els dos hagin atacat.
        pokemon_one_battle.hp = hp_one
        pokemon_two_battle.hp = hp_two

    if hp_one > 0:
        pokemon_winner = pokemon_one.name
        team_one_wins= True
        initial_hp = initial_hp_one
        final_hp = hp_one
        hp_winners = hp_one
        points_earned = calculate_points(final_hp, initial_hp)

    else:
        pokemon_winner = pokemon_two.name
        team_one_wins= False
        initial_hp = initial_hp_two
        final_hp = hp_two
        hp_winners = hp_two
        points_earned = calculate_points(final_hp, initial_hp)

    battle_results = BattleResults(turn=torn, pokemon_winner=pokemon_winner, team_one_wins=team_one_wins, hp_winners=hp_winners, points_winner=points_earned)   

    # Aquí podria anar fent una llista per retornar un log de cada torn
    return log, battle_results


