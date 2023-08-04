import criacao, player, eventos, combate, skills

rodada = 1
vivo = True

#definir nome do personagem duh
nome = input("Nome do personagem: ").strip().title()

print(f"\nBem vindo a arena, {nome}")

escolha = int(input("Escolha sua classe:\n1 - Monge\n2 - Samurai\n3 - Ninja\n"))

#definição de classe e atributos
criacao.init_classe(escolha)

#definição de arma e atributos
criacao.init_arma(player.classe_player)

while rodada <= 5 and combate.vivo == True:
    print(f"RODADA {rodada}")
    eventos.gerar_evento()
    rodada+=1