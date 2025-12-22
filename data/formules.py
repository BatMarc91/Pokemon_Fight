import random

# Fórmules per als combats

    # Velocitat
def calculate_speed(pokemon_speed):
    speed_points = pokemon_speed
    return speed_points

    # Càlculo els valors per a atac vs defensa (Físic):
def calculate_physical_damage(pokemon_physical_damage):
    att_coef = random.randint(75, 125) / 100
    physical_damage = round(pokemon_physical_damage * att_coef, 2)
    return physical_damage

def calculate_physical_defense(pokemon_physical_defense):
    physical_defense = pokemon_physical_defense
    return physical_defense

# Proves per fer algun càlcul a l'hora de definir la velocitat
def choose_first_attack(speed_one: float, speed_two: float):
    if speed_one > speed_two:
        speed_difference = speed_one - speed_two

    return speed_difference

