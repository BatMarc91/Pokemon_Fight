from pydantic import BaseModel

class PokemonModel(BaseModel):
    team_name: str
    name: str

class PokemonStats(PokemonModel):
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int

class TeamModel(BaseModel):
    name: str
    pokemons: list

class TeamStats(BaseModel):
    name: str
    pokemons: list[PokemonModel]

class FightModel(BaseModel):
    num_fight: int
    pokemon_one: PokemonModel
    pokemon_two: PokemonModel


