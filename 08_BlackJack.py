import random

def distribuir_carta():
    """Retorna uma carta aleatória do baralho"""
    cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    carta = random.choice(cartas)
    return carta


def calcular_pontuacao(cartas):
    """Recebe uma lista de cartas e retorna a pontuação calculada a partir das cartas"""
    if sum(cartas) == 21 and len(cartas) == 2:
        return 0

    if 11 in cartas and sum(cartas) > 21:
        cartas.remove(11)
        cartas.append(1)

    return sum(cartas)


def comparar(pontuacao_usuario, pontuacao_computador):
    """Compara a pontuação do usuário pontuacao_usuario contra a pontuação do computador pontuacao_computador."""
    if pontuacao_usuario == pontuacao_computador:
        return "Empate 🙃"
    elif pontuacao_computador == 0:
        return "Perdeu, o oponente tem Blackjack 😱"
    elif pontuacao_usuario == 0:
        return "Ganhou com um Blackjack 😎"
    elif pontuacao_usuario > 21:
        return "Você ultrapassou 21. Você perdeu 😭"
    elif pontuacao_computador > 21:
        return "Oponente ultrapassou 21. Você ganhou 😁"
    elif pontuacao_usuario > pontuacao_computador:
        return "Você ganhou 😃"
    else:
        return "Você perdeu 😤"


def jogar_jogo():
    cartas_usuario = []
    cartas_computador = []
    pontuacao_computador = -1
    pontuacao_usuario = -1
    jogo_finalizado = False

    for _ in range(2):
        cartas_usuario.append(distribuir_carta())
        cartas_computador.append(distribuir_carta())

    while not jogo_finalizado:
        pontuacao_usuario = calcular_pontuacao(cartas_usuario)
        pontuacao_computador = calcular_pontuacao(cartas_computador)
        print(f"Suas cartas: {cartas_usuario}, pontuação atual: {pontuacao_usuario}")
        print(f"Primeira carta do computador: {cartas_computador[0]}")

        if pontuacao_usuario == 0 or pontuacao_computador == 0 or pontuacao_usuario > 21:
            jogo_finalizado = True
        else:
            usuario_deve_distribuir = input("Digite 's' para pegar outra carta, digite 'n' para passar: ")
            if usuario_deve_distribuir == "s":
                cartas_usuario.append(distribuir_carta())
            else:
                jogo_finalizado = True

    while pontuacao_computador != 0 and pontuacao_computador < 17:
        cartas_computador.append(distribuir_carta())
        pontuacao_computador = calcular_pontuacao(cartas_computador)

    print(f"Sua mão final: {cartas_usuario}, pontuação final: {pontuacao_usuario}")
    print(f"Mão final do computador: {cartas_computador}, pontuação final: {pontuacao_computador}")
    print(comparar(pontuacao_usuario, pontuacao_computador))


while input("Você quer jogar uma partida de Blackjack? Digite 's' ou 'n': ") == "s":
    print("\n" * 20)
    jogar_jogo()
