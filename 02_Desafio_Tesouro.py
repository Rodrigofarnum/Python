print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Bem-vindo à Ilha do Tesouro.")
print("Sua missão é encontrar o tesouro.")

print("Você está em uma encruzilhada. Para onde você quer ir?")
cross_road = input("    Digite \"esquerda\" ou \"direita\"\n").lower()
if cross_road == "direita":
    print("Você caiu em um buraco.\n FIM DE JOGO!")
else:
    print("Você chegou a um lago. Há uma ilha no meio do lago.")
    lake = input("  Digite \"esperar\" para esperar um barco ou digite \"nadar\" para atravessar nadando\n").lower()
    if lake == "nadar":
        print("Você é atacado por um crocodilo furioso.\n FIM DE JOGO!")
    else:
        print("Você chega na ilha ileso. Há uma casa com 3 portas.")
        house = input(" Uma vermelha, uma amarela e uma azul. Qual cor você escolhe?\n").lower()
        if house == "vermelha":
            print("É uma sala cheia de fogo.\n FIM DE JOGO!")
        elif house == "azul":
            print("Você entra em uma sala cheia de feras.\n FIM DE JOGO!")
        else:
            print("Parabéns, você encontrou o tesouro!\n VOCÊ VENCEU!")
