import random

#nomes
nmaq = "jknp3000"
njog = str(input("Qual o teu nome amigo??: "))

#placar
pjog = 0
pmaq = 0


#ascii
def pedra():
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

def papel():
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

def tes():
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

def rodada():
    rodmaq = random.randint(1,3)
    rodjog = 0
    
    while rodjog  != 1 and rodjog != 2 and rodjog != 3:

        rodjog = int(input("Você quer ser oq? \n 1(pedra) \n 2(papel) \n 3(tesoura) \n >> "))
    
    return (rodjog, rodmaq)

def vencedor(p1,p2):
    #1 = Pedra, 2 = Papel, 3 = Tesoura
    #p1 = jogador // p2 = bot
    
    ganhador = ""
    jogada =  ""

   
    if p1 == 1 and p2 == 1:
        pedra()
        pedra()
        return "Empatou",  ""


    elif p1 == 1 and p2 == 2:
        pedra()
        papel()
        return f"{nmaq} venceu",  ""


    elif p1 == 1 and p2 == 3:
        pedra()
        tes()
        return f"{njog} venceu", ""


    elif p1 == 2 and p2 == 1:
        papel()
        pedra()
        return f"{njog} venceu", ""

    elif p1 == 2 and p2 == 2:
        papel()
        papel()
        return "Empatou", ""

    elif p1 == 2 and p2 == 3:
        papel()
        tes()
        return f"{nmaq} venceu", ""

    elif p1 == 3 and p2 == 1:
        tes()
        pedra()
        return f"{nmaq} venceu", ""
    
    elif p1 == 3 and p2 == 2:
        tes()
        papel()
        return f"{njog} venceu", ""

    elif p1 == 3 and p2 == 3:
        tes()
        tes()
        return "Empatou", ""

def placar(ganhador):
    global pjog, pmaq
    if ganhador == f"{njog} venceu":
        pjog += 1

    else:
        pmaq += 1

    msg = f"""Placar Geral
Jogador vitorias: {pjog}
Maquina vitorias: {pmaq}"""
    return msg

def sair():
    op = "alefmeda10"
    while op != "s" or "n":
        op = str(input("Deseja sair do jogo? s/n: ")).lower()
        if op == "s":
            return False
        elif op == "n":
            return True

def comeca():
    print(f"Bip, bop. Eu sou{nmaq}")
    gameon = True
    while gameon == True:
        p1, p2 = rodada()
        ganhador, jogada = vencedor(p1,p2)
        print(ganhador)
        print(jogada)
        print(placar(ganhador))
        gameon = sair()

comeca()
 