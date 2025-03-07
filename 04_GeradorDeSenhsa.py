import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Bem-vindo ao Gerador de Senhas PyPassword!")

# Requisitos da senha
nr_letras = int(input("Quantas letras você gostaria na sua senha?\n"))
nr_simbolos = int(input("Quantos símbolos você gostaria?\n"))
nr_numeros = int(input("Quantos números você gostaria?\n"))

# Gerador de senha
lista = []
for i in range(0, nr_letras):
    lista.append(random.choice(letras))
for i in range(0, nr_simbolos):
    lista.append(random.choice(simbolos))
for i in range(0, nr_numeros):
    lista.append(random.choice(numeros))

# Embaralhamento da senha
random.shuffle(lista)

# Organização da senha
senha = ""
caracteres = nr_letras + nr_simbolos + nr_numeros
for i in range(0, caracteres):
   senha += lista[i]

# Finalizando a senha
print(f"Sua nova senha é: {senha}")
