import classes

nome = input("Nome do personagem: ")

print(f"\nBem vindo a arena, {nome}")

escolha = int(input("Escolha sua classe:\n1 - Monge\n2 - Samurai\n3 - Ninja\n"))

classes.init_classe(escolha)
