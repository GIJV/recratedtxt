hp = 0
fv = 0

forc = 0
dex = 0
pre = 0
con = 0

def adicionar(a, b, c, d, e, f): 
    global hp, fv, forc, dex, pre, con

    hp += a
    fv += b
    forc += c
    dex += d
    pre += e
    con += f

def debug():
    print(f"Vida: {hp}\nForça Vital: {fv}\nForça: {forc}\nDestreza: {dex}\nPresença: {pre}\nConstituição: {con}")