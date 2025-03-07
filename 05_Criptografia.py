alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def cesar(texto_original, quantidade_deslocamento, codificar_ou_decodificar):
    texto_saida = ""
    if codificar_ou_decodificar == "decodificar":
        quantidade_deslocamento *= -1

    for letra in texto_original:

        if letra not in alfabeto:
            texto_saida += letra
        else:
            posicao_deslocada = alfabeto.index(letra) + quantidade_deslocamento
            posicao_deslocada %= len(alfabeto)
            texto_saida += alfabeto[posicao_deslocada]
    print(f"Aqui está o resultado {codificar_ou_decodificar}do: {texto_saida}")


continuar = True

while continuar:

    direcao = input("Digite 'codificar' para criptografar, digite 'decodificar' para descriptografar:\n").lower()
    texto = input("Digite sua mensagem:\n").lower()
    deslocamento = int(input("Digite o número do deslocamento:\n"))

    cesar(texto_original=texto, quantidade_deslocamento=deslocamento, codificar_ou_decodificar=direcao)

    reiniciar = input("Digite 'sim' se você quiser continuar. Caso contrário, digite 'não'.\n").lower()
    if reiniciar == "não":
        continuar = False
        print("Adeus")
