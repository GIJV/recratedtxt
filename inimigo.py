atributos = {
    'id': 0,
    'hp': 0,
    'cd': 0,
    'acerto': 0,
    'dano': 0,
    'num_dados': 0,
    'xp_dado': 0,
    'dano_extra': 0
}

def iniciar_inimigo(inimigo):
    if inimigo == 1:
        atributos['hp'] = 30
        atributos['cd'] = 10
        atributos['acerto'] = 0
        atributos['dano'] = 1
        atributos['num_dados'] = 1
        atributos['xp_dado'] = 50
        atributos['dano_extra'] = 3
    elif inimigo == 2:
        atributos['hp'] = 50
        atributos['cd'] = 12
        atributos['acerto'] = 2 
        atributos['dano'] = 1
        atributos['num_dados'] = 2
        atributos['xp_dado'] = 100
        atributos['dano_extra'] = 5
    elif inimigo == 3:
        atributos['hp'] = 100
        atributos['cd'] = 8
        atributos['acerto'] = 5 
        atributos['dano'] = 2
        atributos['num_dados'] = 2
        atributos['xp_dado'] = 200
        atributos['dano_extra'] = 3
    else:
        atributos['hp'] = 150
        atributos['cd'] = 15
        atributos['acerto'] = 7
        atributos['dano'] = 3
        atributos['num_dados'] = 3 
        atributos['xp_dado'] = 400
        atributos['dano_extra'] = 5
