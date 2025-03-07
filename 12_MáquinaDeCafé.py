MENU = {
    "expresso": {
        "ingredientes": {
            "agua": 50,
            "cafe": 18,
        },
        "custo": 1.5,
    },
    "café com leite": {
        "ingredientes": {
            "agua": 200,
            "leite": 150,
            "cafe": 24,
        },
        "custo": 2.5,
    },
    "cappuccino": {
        "ingredientes": {
            "agua": 250,
            "leite": 100,
            "cafe": 24,
        },
        "custo": 3.0,
    }
}

recursos = {
    "agua": 300,
    "leite": 200,
    "cafe": 100,
}

def ligado():
    """This function checks with the machine have resources"""
    if pedido == "reportar":
        print(f"Água: {recursos["agua"]}ml\nLeite:{recursos["leite"]},l\nCafé: {recursos["cafe"]}g\nDinheiro: R${recursos["lucro"]}")
    else:
        ingredientes = MENU[pedido]["ingredientes"]
        for i in ingredientes:
            if recursos[i] - ingredientes[i] < 0:
                print(f"Desculpe, a máquina não tem {i} suficiente para atender ao seu pedido")
                return False
        pagamento()

def pagamento():
    """This function checks the payment (Brazilian coins)"""
    moedas = {
        "cinco" : 0,
        "dez": 0,
        "vinte_e_cinco": 0,
        "cinquenta": 0,
        "um": 0,

    }
    for i in moedas:
        if i == "um":
            x = input(f"Quantas moedas de {i} real você vai inserir?")
            moedas[i] = x
        else:
            x = input(f"Quantas moedas de {i} centavos você vai inserir?")
            moedas[i] = x
    total = float(moedas["cinco"]) * 0.05  + float(moedas["dez"]) * 0.1  + float(moedas["vinte_e_cinco"]) * 0.25 +  float(moedas["cinquenta"]) * 0.5  + float(moedas["um"]* 1)
    if total < MENU[pedido]["custo"]:
        print("Desculpa, isso não é o suficiente. Dinheiro devolvido.")
    else:
        if total > MENU[pedido]["custo"]:
            devolver = total - MENU[pedido]["custo"]
            print(f"Aqui está seu troco R$ {devolver:.2f}.")
        producao()

def producao():
    """This function makes the order"""
    recursos ["lucro"] += MENU[pedido]["custo"]
    for i in recursos:
        if i in MENU[pedido]["ingredientes"]:
            recursos[i] =  recursos[i] - MENU[pedido]["ingredientes"][i]
    print(f"Aqui está seu {pedido}. Aproveite! ☕ ")


#Checks with the machine is ON
recursos ["lucro"] = 0
off = False
while not off:
    pedido = input("O que você deseja? (expresso, café com leite, cappuccino): ")
    if pedido == "off":
        off = True
    else:
        ligado()

