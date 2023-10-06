distancia = float(input("Qual é a distância da sua viagem: "))
print("Você está prestes a começar uma viagem de {} KM".format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
    print("E o preço da sua viagem sera de R${:.2f}".format(preco))
else:
    preco = distancia * 0.45
    print("E o preço da sua viagem será de R${:.2f}".format(preco))