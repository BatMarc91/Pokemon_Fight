import random



def generate_fight(team_one: dict, team_two:dict):
    positions_one = [1, 2, 3, 4, 5, 6]
    positions_one = random.shuffle(positions_one)

    positions_two = [1, 2, 3, 4, 5, 6]
    positions_two = random.shuffle(positions_two)

    fights = {f"combat 1" : 
                {team_one[0]}}
    
    return fights

