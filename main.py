from components.introduction import intro
from components.game_develop import game_develop

# Selecccionar Idioma 
print("Selecciona idioma / Select language:")
print("1 - Català")
print("2 - Español")
print("3 - English")
lang_choice = input("> ")
language = { "1": "cat", "2": "es", "3": "en" }.get(lang_choice, "es")

# Seleccionar difficultat
print("Selecciona dificultad / Choose difficulty:")
print("1 - Principiant / Principiante / Beginner")
print("2 - Intermedi /Intermedio / Mid")
print("3 - Expert / Experto / Expert")
diff_choice = input("> ")
difficulty = { "1": "beginner", "2": "mid", "3": "expert" }.get(diff_choice, "mid")

# Introducció i selecció d'equips
teams = intro(language, difficulty)

marc_team = teams[0]
user_team = teams[1]

# Simulcaió dels combats i mostrar guanyador
game_develop(language, marc_team, user_team)

