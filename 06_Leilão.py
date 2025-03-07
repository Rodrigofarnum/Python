loop = "sim"
dicionario = {}
while loop == "sim":
    nome = input("Qual é o seu nome? ")
    lance = float(input("Qual é o seu lance? R$"))
    dicionario[nome] = lance
    loop = input("Há outros lances? Digite 'sim' ou 'não'. ")
    if loop == "sim":
        espaco = "\n" * 20
        print(espaco)

vencedor = 0
for chave in dicionario:
        if dicionario[chave] > vencedor:
            vencedor = dicionario[chave]

print(f"O vencedor é {nome} com um lance de R${vencedor}")
