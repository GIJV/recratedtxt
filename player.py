classe_player = None
arma_player = None

atributos = {
    'hp': 0,
    'fv': 0,
    'cd': 0,
    'forc': 0,
    'dex': 0,
    'pre': 0,
    'con': 0,
    'level': 1,
    'xp': 0,
    'dano_extra': 0,
    'maxhp': 0,
    'maxfv': 0
}

atributos_arma = {
    'acerto': 0,
    'dano': 0,
    'num_dados': 0,
    'dano_extra': 0
}

def definir_classe(classe): 
    global classe_player

    atributos['hp'] = classe[1] + (atributos['con'] * 10)
    atributos['fv'] = classe[2] + (atributos['pre'] * 10)
    atributos['forc'] = classe[3]
    atributos['dex'] = classe[4]
    atributos['pre'] = classe[5]
    atributos['con'] = classe[6]
    atributos['cd'] = classe[7] + atributos['dex']
    atributos['maxhp'] = classe[8]
    atributos['maxfv'] = classe[9]

    if classe[0] == 1:
        classe_player = "Monge"
    elif classe[0] == 2:
        classe_player = "Samurai"
    else:
        classe_player = "Ninja"

def definir_arma(arma):
    global arma_player

    atributos_arma['acerto'] = arma[1]
    atributos_arma['dano'] = arma[2]
    atributos_arma['num_dados'] = arma[3]
    atributos_arma['dano_extra'] = arma[4]

    if arma[0] == 1:
        arma_player = 'Bastão'
    elif arma[0] == 2:
        arma_player = 'Manopla'
    elif arma[0] == 3:
        arma_player = 'Chicote'
    elif arma[0] == 4:
        arma_player = 'Katana'
    elif arma[0] == 5:
        arma_player = 'Escudo'
    elif arma[0] == 6:
        arma_player = 'Lança'
    elif arma[0] == 7:
        arma_player = 'Wakizashi'
    elif arma[0] == 8:
        arma_player = 'Shuriken'
    elif arma[0] == 9:
        arma_player = 'Kama'

    print(arma_player, atributos_arma)