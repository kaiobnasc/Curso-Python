velocidade = int(input("Qual é a velocidade do carro: "))

if velocidade < 80:
    print("Tenha um bom dia, dirija com cuidado!")
else:
    multa = (velocidade - 80) * 7
    print("Você está acima do permitido. Sua velocidade é {} e sua multa é de R${}".format(velocidade, multa))