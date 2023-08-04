import player

# [id, Hp, Fv, Forc, Dex, Pre, Con, CD] id: 1 = Monge, 2 = samurai, 3 = ninja
classes = {
    'monge': [1, 50, 100, 0, 1, 2, 1, 10, 50, 100],
    'samurai': [2, 100,25,2,0,0,2,5, 100, 25],
    'ninja': [3, 25,50,1,2,1,0,15, 25, 50]
}

#[id, acerto, tipo do dano, numero de dados]
#1 = d4, 2 = d6, 3 = d8, 4 = d10, 5 = d12, 6 = d20
armas = {
    'bastão': [1,5,1,3,player.atributos['forc']],
    'manopla': [2,5,3,1,(player.atributos['forc'] * 2)],
    'chicote': [3,3,2,2,player.atributos['dex']],
    'katana': [4,5,4,1,max(player.atributos['forc'],player.atributos['dex'])],
    'escudo': [5,3,5,1,player.atributos['forc']],
    'lança': [6,5,3,2,player.atributos['forc']],
    'wakizashi': [7,5,1,1,player.atributos['dex']],
    'shuriken': [8,5,1,1,player.atributos['forc'] + player.atributos['dex']],
    'kama': [9,3,2,1,player.atributos['dex']]
}

def init_classe(escolha):
    if escolha == 1:
        player.definir_classe(classes['monge'])
    elif escolha == 2:
        player.definir_classe(classes['samurai'])
    else:
        player.definir_classe(classes['ninja'])

def init_arma(classe):

    print(classe)

    escolha = None 

    if classe == 'Monge':
        escolha = int(input("Escolha sua arma inicial: \n1 - Bastão\n2 - Manopla\n3 - Chicote\n"))
        if escolha == 1:
            player.definir_arma(armas['bastão'])
        elif escolha == 2:
            player.definir_arma(armas['manopla'])
        else:
            player.definir_arma(armas['chicote'])
    elif classe == 'Samurai':
        escolha = int(input("Escolha sua arma inicial: \n1 - Katana\n2 - Escudo\n3 - Lança\n"))
        if escolha == 1:
            player.definir_arma(armas['katana'])
        elif escolha == 2:
            player.definir_arma(armas['escudo'])
        else:
            player.definir_arma(armas['lança'])
    else:
        escolha = int(input("Escolha sua arma inicial: \n1 - Wakizashi\n2 - Shuriken\n3 - Kama\n"))
        if escolha == 1:
            player.definir_arma(armas['wakizashi'])
        elif escolha == 2:
            player.definir_arma(armas['shuriken'])
        else:
            player.definir_arma(armas['kama'])