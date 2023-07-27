import personagem

def init_classe(classe):
    if classe == 1:
        personagem.adicionar(50,100,0,1,2,1)
        personagem.debug()
    elif classe == 2:
        personagem.adicionar(100,25,2,0,0,2)
        personagem.debug()
    elif classe == 3:
        personagem.adicionar(25,50,1,2,1,0)
        personagem.debug()