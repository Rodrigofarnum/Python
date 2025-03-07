def adicionar(n1, n2):
    return n1 + n2


def subtrair(n1, n2):
    return n1 - n2


def multiplicar(n1, n2):
    return n1 * n2


def dividir(n1, n2):
    return n1 / n2


operacoes = {
    "+": adicionar,
    "-": subtrair,
    "*": multiplicar,
    "/": dividir,
}

def calculadora():
    deve_acumular = True
    num1 = float(input("Qual é o primeiro número?: "))

    while deve_acumular:
        for simbolo in operacoes:
            print(simbolo)
        simbolo_operacao = input("Escolha uma operação: ")
        num2 = float(input("Qual é o próximo número?: "))
        resposta = operacoes[simbolo_operacao](num1, num2)
        print(f"{num1} {simbolo_operacao} {num2} = {resposta}")

        escolha = input(f"Digite 'y' para continuar calculando com {resposta}, ou digite 'n' para iniciar um novo cálculo: ")

        if escolha == "y":
            num1 = resposta
        else:
            deve_acumular = False
            print("\n" * 20)
            calculadora()


calculadora()
