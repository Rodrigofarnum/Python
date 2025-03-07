print("Bem-vindo ao calculador de gorjetas!")
conta = float(input("Qual foi o valor total da conta? R$ "))
gorjeta = float(input("Qual porcentagem de gorjeta você gostaria de dar? 10 12 15 "))
pessoas = int(input("Quantas pessoas vão dividir a conta? "))

gorjeta /= 100
total = (conta * gorjeta + conta) / pessoas

print(f"Cada pessoa deve pagar: R$ {(total):.2f}")
