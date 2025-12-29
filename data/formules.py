import random

# Fórmules per als combats
# Velocitat
def calculate_speed(pokemon_speed):
    speed_points = pokemon_speed
    return speed_points

def choose_first_attack(speed_one, speed_two):
    # Cas especial: mateixa velocitat → 50/50
    if speed_one == speed_two:
        return random.choice([1, 2])

    # Identifiquem el més ràpid
    if speed_one > speed_two:
        faster = 1
        speed_fast = speed_one
        speed_slow = speed_two
    else:
        faster = 2
        speed_fast = speed_two
        speed_slow = speed_one

    # Diferència percentual de velocitat
    speed_advantage = (speed_fast - speed_slow) / speed_slow  # ex: 0.2 = 20%

    # Convertim l'avantatge en probabilitat
    base_probability = 0.55  # 55% mínim
    bonus = min(speed_advantage, 0.30)  # límit del 30%
    probability_fast = base_probability + bonus  # màxim 85%

    # Tirada aleatòria
    roll = random.random()  # valor entre 0 i 1

    if roll < probability_fast:
        return faster
    else:
        return 1 if faster == 2 else 2

# Càlculo els valors per a atac vs defensa (Físic):
def physical_attack(attack_damage, defense_damage):
    """Funció retorna el dany d'atac realitzat"""

    damage = attack_damage - defense_damage

    if damage < 0:
        damage = 2

    return damage

def calculate_physical_damage(pokemon_physical_damage):
    att_coef = random.randint(75, 125) / 100
    physical_damage = int(round(pokemon_physical_damage * att_coef, 0))

    return physical_damage

def calculate_physical_defense(pokemon_physical_defense):
    physical_defense = int(round(pokemon_physical_defense, 0))

    return physical_defense

def calculate_points(final_hp, initial_hp):
    """Funció que retorna els punts per haver guanyat un combat"""

    # Calculo els punts en funció del rati de hp perdut
    hp_ratio = final_hp / initial_hp

    if hp_ratio >= 0.80:
        return 5
    elif hp_ratio >= 0.60:
        return 4
    elif hp_ratio >= 0.40:
        return 3
    elif hp_ratio >= 0.20:
        return 2
    else:
        return 1


