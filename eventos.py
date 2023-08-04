import combate, skills
from random import randint

def gerar_evento():
    evento = randint(1, 2)

    if evento == 1:
        print("Hora do pau")
        inimigo = randint(1, 4)
        combate.combate(inimigo)
    elif evento == 2:
        print("Bençao de xp")
        skills.ganhar_xp(50)
    else:
        print("Toma skill")