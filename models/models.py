from pydantic import BaseModel

class PokemonModel(BaseModel):
    name: str
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int

class TeamModel(BaseModel):
    name: str
    pokemons: list

class FightModel(BaseModel):
    pokemon_one: PokemonModel()
    pokemon_two: PokemonModel()


