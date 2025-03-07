import random

# Galeria
pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
imagens_do_jogo = [pedra, papel, tesoura]

# Turno do jogador
Jogador = int(input("O que você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura.\n"))
print(imagens_do_jogo[Jogador])

# Turno do NPC
NPC = random.randint(0,2)
print("O computador escolheu:")
print(imagens_do_jogo[NPC])

# Resultado
if Jogador == 0 and NPC == 1:
    print("Você perdeu!")
elif Jogador == 0 and NPC == 2:
    print("Você ganhou!")
elif  Jogador == 1 and NPC == 0:
    print("Você ganhou!")
elif Jogador == 1 and NPC == 2:
    print("Você perdeu!")
elif Jogador == 2 and NPC == 0:
    print("Você perdeu!")
elif Jogador == 2 and NPC == 1:
    print("Você ganhou!")
else:
    print("Empate!")
