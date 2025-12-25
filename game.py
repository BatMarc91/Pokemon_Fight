from data.env import marc_beginner, marc_mid, marc_expert
from components.search_pokemon import search_pokemon
from models.models import PokemonModel, TeamModel, FightModel
from components.generate_fight import generate_fight
from narrativa_game.narrativa import intro

# Introducció i selecció d'equips
user_team = intro()

print(f"""
    Genial, aquí tens el teu equip: {user_team})
    -------------------------------------------
    """)

for pokemon in marc_team:
    print(f"  • {pokemon}")

print("""
    -------------------------------------------
    """)

print("Ara anem a fer el sorteig de cada un dels 6 enfrontaments")

sorteig = generate_fight(marc_team, user_team)

for fight in sorteig:
    print(f"  • {fight}")









