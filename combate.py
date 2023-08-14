from random import randint
import player, inimigo, skills

vivo = True

crit = False

dano_player = 0

cd_reduc = False

def dados(valor):
#1 = d4, 2 = d6, 3 = d8, 4 = d10, 5 = d12, 6 = d20
    if valor == 1:
        return randint(1, 4)
    elif valor == 2:
        return randint(1, 6)
    elif valor == 3:
        return randint(1, 8)
    elif valor == 4:
        return randint(1, 10)
    elif valor == 5:
        return randint(1, 12)
    elif valor == 6:
        return randint(1, 20)
    
def multiplos_dados(quantidade, valor):
    soma = 0
    for _ in range(quantidade):
        roll = dados(valor)
        soma += roll
        for index, value in player.atributos_arma.items():
            if index == 0 and value in [7,8,9]:
                if roll == 4:
                    quantidade += 1
    return soma

def maior_dado(quantidade):
    resultados = []
    for _ in range(quantidade):
        roll = randint(1,20)
        resultados.append(roll)
    return max(resultados)

def combate(enemy):
    global crit, dano_player, cd_reduc, vivo

    buff = 0
    hp = player.atributos['hp']

    inimigo.iniciar_inimigo(enemy)

    while True:
        #checar player
        if hp <= 0 and skills.kanyou == False:
            print("Foi de gamas")
            vivo = False
            break
        elif hp <= 0 and skills.kanyou == True:
            print("Kanyou ativado")
            player.atributos['hp'] += (player.atributos['maxhp'] / 2)
            skills.kanyou = False

        if enemy == 1:
            print("Você está enfrentando Associado da Raanabi")
        elif enemy == 2:
            print("Você está enfrentando Kremess")
        elif enemy == 3:
            print("Você está enfrentando Jugger & Larry")
        else:
            print("Você está enfrentando Cripgon")

        print(f"Sua vida: {player.atributos['hp']}/{player.atributos['maxhp']}\nSua Força Vital: {player.atributos['fv']}/{player.atributos['maxfv']}\nVida inimigo: {inimigo.atributos['hp']}")
        acao = int(input("MAKE YOUR CHOICE: \n1 - atacar\n2 - Skills\n3 - Defender\n"))
            #ação player
        if acao == 1:
            #rodar dado de acerto
            roll = dados(6)
            if roll == 20:
                player.atributos_arma['num_dados'] += 1
                crit = True
            acerto_player = player.atributos_arma['acerto'] + roll
            print(f"\nacerto: {acerto_player}\n")
            #acertou = rodar dado dano
            if acerto_player >= inimigo.atributos['cd']:
                if skills.ambis == True:
                    buff += 1     
                if skills.artesa == True:
                    buff += 1
                dados = player.atributos_arma['num_dados']
                dano = player.atributos_arma['dano']
                roll = multiplos_dados((dados + buff), dano)
                dano_player = roll + player.atributos_arma['dano_extra']
                if crit == True:
                    crit = False
                    player.atributos_arma['num_dados'] -= 1
                inimigo.atributos['hp'] -= dano_player
                print(f"\nVoce causou: {dano_player} de dano\n")
            else:
                print("\nerrou\n")
        elif acao == 2:
            skills.escolher_skill()
        elif acao == 3:
            player.atributos['cd'] += 5
            print("voce se defendeu")
        #checar inimigo

        if enemy == 4 and cd_reduc == True:
            player.atributos['cd'] += 3
            cd_reduc = False

        if enemy == 3:
            hp = inimigo.atributos['hp']
            if hp <= 50:
                inimigo.atributos['hp'] += 20
                print("Jugger & Larry usaram: Ressurection - Ao chegar em 50HP ou menos, +20hp")

        if hp <= 0:
            print("Você venceu, toma tua recompensa")
            player.ganhar_xp(inimigo.atributos['xp_dado'])
            break
        else:   
            # ação inimigo
            if enemy == 1:
                chance = randint(1,100)
                if chance <= 5:
                    acao_inimigo = 3
                elif chance > 5 and chance <= 15:
                    acao_inimigo = 2
                else:
                    acao_inimigo = 1 
            elif enemy == 2:
                chance = randint(1,100)
                if chance <= 25:
                    acao_inimigo = 3
                elif chance > 25 and chance <= 50:
                    acao_inimigo = 2
                else:
                    acao_inimigo = 1 
            elif enemy == 3:
                chance = randint(1,100)
                if chance <= 10:
                    acao_inimigo = 3
                elif chance > 10 and chance <= 45:
                    acao_inimigo = 1
                else:
                    acao_inimigo = 2
            else:
                chance = randint(1,100)
                if chance <= 33:
                    acao_inimigo = 3
                elif chance > 33 and chance <= 66:
                    acao_inimigo = 1
                else:
                    acao_inimigo = 2
            #ataque normal
            if acao_inimigo == 1:
                roll = dados(6)
                acerto_inimigo = inimigo.atributos['acerto'] + roll
                if acerto_inimigo >= player.atributos['cd']:
                    print(f"Acerto do inimigo: {acerto_inimigo}")
                    print("Inimigo te acertou")
                    roll = multiplos_dados(inimigo.atributos['num_dados'],inimigo.atributos['dano'])
                    dano_inimigo = roll + inimigo.atributos['dano_extra']
                    player.atributos['hp'] -= dano_inimigo
                    print(f"Voce tomou {dano_inimigo} de dano")
            #skill
            elif acao_inimigo == 2:
                if enemy == 1:
                    print("Inimigo usou skill: Esforço Maximo - Associado da Raanabi recebe +1d4")
                    inimigo.atributos['num_dados'] += 1
                elif enemy == 2:
                    skill = randint(1,2)
                    if skill == 1:
                        print("Inimigo usou skill: Jaqueta de Couro - Kremess recebe +10 HP")
                        inimigo.atributos['hp'] += 10
                    elif skill == 2:
                        print("Inimigo usou skill: Suplex Definitivo - Kremess pode curar o dano recebido no turno")
                        roll = randint(1,20)
                        if roll + player.atributos['forc'] + player.atributos['dex'] < 15:
                            print("Kremes se curou")
                            inimigo.atributos['hp'] += dano_player
                        else:
                            print("Falha na habilidade")
                elif enemy == 3:
                    print("Inimigo usou skill: Trovão Celestial - Causa 2d10 dano se acertar")
                    acerto_inimigo = maior_dado(2) + 5
                    if acerto_inimigo > player.atributos['cd']:
                        roll = multiplos_dados(2, 4)
                    else:
                        print("inimigo errou")
                else:
                    skill = randint(1, 100)
                    if skill <= 30:  
                        print("Inimigo usou skill: Psicose - Faz o jogador se atacar")
                        roll = dados(6)
                        if roll + player.atributos['pre'] < 15:
                            roll = multiplos_dados(player.atributos_arma['num_dados'],player.atributos_arma['dano'])
                            dano_player = roll + player.atributos_arma['dano_extra']
                            player.atributos['hp'] -= dano_player
                    else:
                        print("Inimigo usou skill: Mestre das Sombras - -3 Acerto ao Player no próximo turno")
                        player.atributos['cd'] -= 3
                        cd_reduc = True
                        
            #defend
            elif acao_inimigo == 3:
                inimigo.atributos['cd'] += 5
                print("inimigo se defendeu")
        #fim de turno

        if skills.buddy == True:
            if acerto_player >= inimigo.atributos['cd']:
                roll = multiplos_dados(inimigo.atributos['num_dados'],inimigo.atributos['dano'])
                inimigo.atributos['hp'] -= roll
                print(f"{skills.nome_buddy} causou {roll} de dano")
            else:
                print(f"{skills.nome_buddy} errou o ataque")

        if acao == 2:
            player.atributos['cd'] -= 5
        if acao_inimigo == 2:
            inimigo.atributos['cd'] -= 5
