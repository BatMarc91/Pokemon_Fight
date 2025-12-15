from env import marc_team
from create_team import get_team_stats, select_team

def play_game():
    """Funció que executa tot el joc"""

    print(f"""
    Benvingut al joc de combats de Pokemon. 
        Avui desafiaràs a Marc i el seu equip Pokemon format per:
            - {marc_team}
    """)

    stats_team_marc = get_team_stats(marc_team)

    print("""Qui seran els escullits per al combat?""")

    stats_user_team = select_team()

    print(f"""Els dos equips que s'enfrontaran son:""")
    
    for pokemon in stats_team_marc:
        print()



play_game()

#stats_team_marc = get_team_stats(marc_team)
#print(stats_team_marc)







