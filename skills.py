from random import randint
import combate, inimigo, player

level_cap = 50
id = 2

custo = 0

dokudamip = False
conjurador = False
ambis = False
artesa = False
armadura = False
buddy = False
nome_buddy = None
kanyou = False

ativas = {
    'dokudami': [True, "Recupera 1d4 HP e 2/6FV", 1],
    'gravitum': [False, f"1d6+{player.atributos['pre']} - 3/6FV",0],
    'dark sun': [False, f"2d10+{player.atributos['pre']} - 8FV",0],
    'metal armor': [False, f"2+{player.atributos['pre']}+cd até o fim do turno - 5FV",0],
    'shadow claw': [False, f"2d6+{player.atributos['pre']} - 6/9FV",0],
    'eco amplifico': [False, f"Não escolha esse golpe - 10FV",0]
}

if armadura == True:
    player.atributos['cd'] += 3

def level_up(level):
    global ambis, artesa, armadura, buddy, nome_buddy, kanyou, conjurador, dokudamip, atributos, id

    if level == 2:
        escolha = int(input("Qual skill você quer?\n1 - Ambidestria - Ambidestria - Arma ganha mais um dado do mesmo tipo\n2 - Gravitum - 1d6 + PRE\n3 - Dokudami+ - Recuperaçao do Dokudami aumenta para 2d6"))
        if escolha == 1:
            ambis = True
        elif escolha == 2:
            ativas['gravitum'][0] = True
            ativas['gravitum'][2] = id
            id+=1
        elif escolha == 3:
            dokudamip = True
    elif level == 3:
        escolha = int(input("Qual skill você quer?\n1 - Armadura Revestida - +3CD permanente\n2 - Conjurador Circular - Aumenta o dano de suas habilidades de dano em +1 dado\n3 - Dark Sun Awakening - 2d10+PRE"))
        if escolha == 1:
            armadura = True
        elif escolha == 2:
            conjurador = True
        elif escolha == 3:
            ativas['dark sun'][0] = True
            ativas['dark sun'][2] = id
            id+= 1
    elif level == 4:
        escolha = int(input("Qual skill você quer?\n1 - Mestra Artesã - Arma ganha mais um dado do mesmo tipo\n2 - Metal Armor - +(PRE)CD até o fim do turno\n3 - Shadow Claw - 2d6+PRE"))
        if escolha == 1:
            artesa = True
        elif escolha == 2:
            ativas['metal armor'][0] = True
            ativas['metal armor'][2] = id
            id+=1
        elif escolha == 3:
            ativas['shadow claw'][0] = True
            ativas['shadow claw'][2] = id
            id+=1
    elif level == 5:
        escolha = int(input("Qual skill você quer?\n1 - Buddy - Recebe um companheiro que o ajuda em combate, causando dano adicional baseado na arma de escolha\n2 - Eco Amplifico - Dano somado ao dano do turno passado + PRE\n3 - Kanyou - Se vida chegar a 0 ou menos, revive com HP 50%"))
        if escolha == 1:
            buddy = True
        elif escolha == 2:
            ativas['eco amplifico'][0] = True
            ativas['eco amplifico'][2] = id
            id+=1
        elif escolha == 3:
            kanyou = True

def escolher_skill():
    count = 1

    for atributo, valor in ativas.items():
        if valor[0] == True:
            print(f"{count} - {atributo}: {valor[1]}")
            count += 1

    escolha = int(input("Qual skill deseja usar? "))
    for atributo, lista in ativas.items():
        if lista[2] == escolha:
            print(atributo)
            usar_skill(atributo)
            break

def usar_skill(skill):
    global custo
    if skill == 'dokudami':
        #Dokudami - Recupera 1d4 HP e FV / Dokudami+ 2d6 HP e FV 
        if dokudamip == False:
            roll = randint(1,4)
            player.atributos['hp'] += roll
            player.atributos['fv'] += roll
            print(f"curou {roll} de vida")
        else:
            roll = combate.multiplos_dados(2,2)
            player.atributos['hp'] += roll
            player.atributos['fv'] += roll
            print(f"Curou {roll} de vida")
    elif skill == 'gravitum':
        #Gravitum - 1d6+PRE
        if conjurador == False:
            custo = 3
            player.atributos['fv'] -= custo
            roll = randint(1,6)
            dano = roll + player.atributos['pre']
            inimigo.atributos['hp'] -= dano
            print(f"Inimigo tomou {dano} de dano")
        else:
            custo = 6
            player.atributos['fv'] -= custo
            roll = combate.multiplos_dados(2,2)
            dano = roll + player.atributos['pre']
            inimigo.atributos['hp'] -= dano
            print(f"Inimigo tomou {dano} de dano")
    elif skill == 'dark sun':
        #Dark Sun Awakening - 2d10+PRE
        custo = 8
        player.atributos['fv'] -= custo
        roll = combate.multiplos_dados(2,4)
        dano = roll + player.atributos['pre']
        inimigo.atributos['hp'] -= dano
        print(f"DAI ENKAI!!!!!!\nVocê brilhou como o sol causando {dano} de dano")
    elif skill == 'metal armor':
        #Metal Armor - +(PRE)CD até o fim do turno
        custo = 5
        player.atributos['fv'] -= custo
        atributos['cd'] += 2 + player.atributos['pre']
    elif skill == 'shadow claw':
        #Shadow Claw - 2d6+PRE
        if conjurador == False:
            custo = 6
            player.atributos['fv'] -= custo
            roll = combate.multiplos_dados(2,2)
            dano = roll + player.atributos['pre']
            inimigo.atributos['hp'] -= dano
            print(f"Você causou {dano} de dano")
        else:
            custo = 9
            player.atributos['fv'] -= custo
            roll = combate.multiplos_dados(3,2)
            dano = roll + player.atributos['pre']
            inimigo.atributos['hp'] -= dano
            print(f"Você causou {dano} de dano")
    elif skill == 'eco amplifico':
        #Eco Amplifico - Dano somado ao dano do turno passado + PRE
        custo = 10
        player.atributos['fv'] -= custo
        buff = 0
        if ambis == True:
            player.atributos['fv'] -= 2
            buff += 1
        if artesa == True:
            player.atributos['fv'] -= 2
            buff += 1
        eco = combate.dano_player
        roll = combate.multiplos_dados((player.atributos_arma['num_dados'] + buff),player.atributos_arma['dano'])
        dano = roll + player.atributos_arma['dano_extra'] + eco + player.atributos['pre']
        inimigo.atributos['hp'] -= dano
        print(f"Você causou {dano} de dano")
        
def ganhar_xp(xp):
    global level_cap

    print(f"voce ganhou {xp} de xp")

    player.atributos['xp'] += xp

    while player.atributos['xp'] >= level_cap:
        player.atributos['level'] += 1
        print(f"seu nivel é {player.atributos['level']}")
        level_up(player.atributos['level'])
        level_cap = level_cap * 2