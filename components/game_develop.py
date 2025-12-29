import time
from components.generate_fight import generate_fight
from components.pokemon_fight import battle
from components.texts.manager import get_text

def game_develop(language, marc_team, user_team):
    time.sleep(1)
    print(get_text(language, "user_team_prepared"))
    time.sleep(1)

    for pokemon in user_team.pokemons:
        print(f"  🔹 {pokemon}")
        time.sleep(0.4)

    time.sleep(0.5)
    print("""
    ══════════════════════════════════════════
    """)

    time.sleep(1)
    print(get_text(language, "text_drawing"))
    time.sleep(1.5)

    sorteig = generate_fight(marc_team, user_team)

    team_one_points = 0
    team_two_points = 0

    for enfrontament in sorteig:
        time.sleep(1)
        print(f"""
    {get_text(language, "text_battle")} {enfrontament.num_fight}
    -------------------------------------------
    """)
        time.sleep(1)

        print(
            f"    🟥 {enfrontament.pokemon_one.name} "
            f"({enfrontament.pokemon_one.team_name})"
        )
        time.sleep(0.5)

        print("        🆚")
        time.sleep(0.5)

        print(
            f"    🟦 {enfrontament.pokemon_two.name} "
            f"({enfrontament.pokemon_two.team_name})"
        )

        time.sleep(1.5)
        print(get_text(language, "battle_begins"))
        time.sleep(1)

        # Calculo el log de la batalla [0] i el BattleResults [1]
        batalla = battle(enfrontament.pokemon_one, enfrontament.pokemon_two)

        log_torns = batalla[0]
        pokemon_winner = batalla[1].pokemon_winner
        team_one_wins = batalla[1].team_one_wins
        hp_winner = batalla[1].hp_winners
        points_winner = batalla[1].points_winner

        # Acumulo punts a l'equip guanyador
        if team_one_wins:
            team_one_points += points_winner
        
        else:
            team_two_points += points_winner

        for torn, atacs in log_torns.items():
            time.sleep(1)
            print(f"""
            {get_text(language, "turn")} {torn}
                ⚡ {atacs["pokemon_one"]} {get_text(language, "attack")} {atacs["pokemon_two"]}
                💥 {get_text(language, "damage")} {atacs["damage_one"]}
                ❤️ {get_text(language, "hp")} {atacs["hp_two"]}
            """)

        time.sleep(1)
        print(f"""
    -------------------------------------------
    🏁 {get_text(language, "battle_ends")}
            {pokemon_winner} {get_text(language, "battle_hp_resume")} {hp_winner} -> {points_winner} {get_text(language, "battle_points_resume")}
    -------------------------------------------
    """)
        time.sleep(1)

    if team_one_points > team_two_points:
        winner_team = marc_team
        points_winner = team_one_points

    else:
        winner_team = user_team
        points_winner = team_two_points

    time.sleep(2)
    print(f"{get_text(language, "final_results")} {user_team.name}")


    time.sleep(3)
    print(f"""
    🎉 {get_text(language, "winner")} 🎉

            🏅 {winner_team.name.upper()} 🏅
    """)

    time.sleep(1.5)
    print(get_text(language, "game_ends"))