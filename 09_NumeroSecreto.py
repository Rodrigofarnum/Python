from random import randint

# Níveis de dificuldade
TENTATIVAS_NIVEL_FACIL = 10
TENTATIVAS_NIVEL_DIFICIL = 5


# Função para verificar o palpite do usuário com a resposta correta
def verificar_resposta(palpite_usuario, resposta_correta, tentativas):
    """Verifica a resposta com o palpite, retorna o número de tentativas restantes."""
    if palpite_usuario > resposta_correta:
        print("Muito alto.")
        return tentativas - 1
    elif palpite_usuario < resposta_correta:
        print("Muito baixo.")
        return tentativas - 1
    else:
        print(f"Você acertou! A resposta era {resposta_correta}")


# Função para definir a dificuldade
def definir_dificuldade():
    nivel = input("Escolha uma dificuldade. Digite 'facil' ou 'dificil': ")
    if nivel == "facil":
        return TENTATIVAS_NIVEL_FACIL
    else:
        return TENTATIVAS_NIVEL_DIFICIL


def jogo():
    # Escolher um número aleatório entre 1 e 100.
    print("Bem-vindo ao Jogo de Adivinhação de Números!")
    print("Estou pensando em um número entre 1 e 100.")
    resposta = randint(1, 100)
    print(f"Psit, a resposta correta é {resposta}")

    tentativas = definir_dificuldade()

    # Repetir a funcionalidade de adivinhar se o usuário errar
    palpite = 0
    while palpite != resposta:
        print(f"Você tem {tentativas} tentativas restantes para adivinhar o número.")
        # Deixe o usuário adivinhar um número
        palpite = int(input("Faça um palpite: "))
        # Acompanhar o número de tentativas e reduzir 1 se o usuário errar
        tentativas = verificar_resposta(palpite, resposta, tentativas)
        if tentativas == 0:
            print("Você ficou sem tentativas, você perdeu.")
            return
        elif palpite != resposta:
            print("Tente novamente.")


jogo()
