<p align="center">
  <img src="assets/banner.png" alt="Pokemon Battle Simulator Banner">
</p>

🕹️ Pokémon Battle Simulator

⚔️ Un simulador de combates Pokémon por terminal, con lógica propia de batalla, soporte multiidioma y niveles de dificultad.

📌 Descripción

Pokémon Battle Simulator es un juego ejecutable desde terminal que simula combates Pokémon entre dos equipos de 6 criaturas.
El jugador elige idioma, dificultad y su propio equipo, mientras el sistema calcula estadísticas, emparejamientos y resultados de combate de forma automática.

El proyecto está diseñado con una arquitectura modular, pensada para crecer hacia:

interfaz gráfica (Pygame)

aplicación web (API + frontend)

nuevas reglas de combate

🎮 Características principales

🌍 Selección de idioma (preparado para ES / EN / CAT)

🎚️ Sistema de dificultad

Principiante

Intermedio

Experto

🎲 Sorteo aleatorio de enfrentamientos

⚔️ Simulación de combates 1vs1

📊 Sistema de puntos basado en HP restante

⏱️ Narrativa cinemática con pausas

🧠 Lógica desacoplada del texto

🧩 Código escalable y modular

🧱 Arquitectura del proyecto
    Pokemon_Battle/
    │
    ├── main.py                     # Script principal
    │
    ├── components/
    │   ├── pokemon_fight.py        # Lógica de combate
    │   ├── generate_fight.py       # Sorteo de enfrentamientos
    │   ├── search_pokemon.py       # Consulta de Pokémon
    │   └── texts/
    │       └── manager.py          # Gestión de idiomas
    │
    ├── data/
    │   ├── env.py                  # Equipos por dificultad
    │   ├── formules.py             # Cálculos (daño, velocidad…)
    │   └── texts/
    │       ├── es.py               # Textos en español
    │       ├── en.py               # Textos en inglés
    │       └── cat.py              # Textos en catalán
    │
    ├── models/
    │   ├── models.py               # Pokémon, Team, Fight (Pydantic)
    │   └── battle.py               # Pokémon en combate
    │
    └── assets/
        └── banner.png              # Imágenes para el README

⚔️ Sistema de combate (resumen)

    Cada Pokémon tiene stats base:

        HP

        Ataque / Defensa

        Ataque especial / Defensa especial

        Velocidad

    🏁 Inicio del combate

        El Pokémon más rápido tiene más probabilidad de atacar primero

        Se añade un factor aleatorio para evitar resultados deterministas

💥 Daño

    El daño se calcula usando:

        stats del atacante

        stats del defensor

        factor aleatorio controlado

        Siempre se inflige al menos 2 puntos de daño

🏆 Puntuación

    El Pokémon ganador aporta puntos a su equipo

    Los puntos dependen del porcentaje de HP restante respecto al HP inicial

🗣️ Sistema de idiomas

    Los textos del juego están completamente desacoplados del código:

        from data.texts.en import title, sub_title, champion_presentation


    Esto permite:

        añadir nuevos idiomas fácilmente

        reutilizar la lógica en web o Pygame

        mantener el código limpio y legible

🎚️ Sistema de dificultad

    La dificultad afecta directamente al equipo rival:

    Dificultad	Equipo rival
        Beginner	Pokémon básicos
        Mid	Equipo equilibrado
        Expert	Pokémon fuertes y rápidos

    Definidos en data/env.py.

▶️ Cómo ejecutar el juego
python main.py


Sigue las instrucciones en pantalla para:

    Elegir idioma

    Elegir dificultad

    Crear tu equipo

    Disfrutar del combate ⚔️

🚀 Futuras mejoras

    🎨 Interfaz gráfica con Pygame

    🌐 Versión web (API + frontend)

        Control de tipos para daño de ataque vs defensa

    🧠 Habilidades Pokémon

    🧪 Estados alterados

    💾 Guardado de partidas

    📈 Estadísticas históricas

🧑‍💻 Tecnologías utilizadas

    🐍 Python

    📦 Pydantic

    🎲 Random

    ⏱️ Time

    (Preparado para FastAPI / Pygame)

🙌 Autor

    Desarrollado como proyecto de aprendizaje y portfolio.

    “Diseñado para aprender arquitectura, lógica de juego y buenas prácticas en Python.”

⭐ ¿Te ha gustado?

    ¡Deja una estrella ⭐ en el repositorio y siéntete libre de proponer mejoras o forks!

