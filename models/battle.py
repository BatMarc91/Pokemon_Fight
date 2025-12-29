from pydantic import BaseModel
from data.formules import calculate_speed, calculate_physical_damage, calculate_physical_defense

class PokemonInBattle():
    def __init__(self, team_name:str, name:str, hp: int,attack: int,defense: int,special_attack: int,special_defense: int, speed: int):
        self.team_name = team_name
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed

    def speed_points(self):
        speed = calculate_speed(self.speed)
        return speed

    def physic_damage(self):
        attack = calculate_physical_damage(self.attack)
        return attack
    
    def defense_damage(self):
        defense = calculate_physical_defense(self.defense)
        return defense

class BattleResults(BaseModel):
    turn: int
    pokemon_winner: str
    team_one_wins: bool
    hp_winners: int
    points_winner: int
