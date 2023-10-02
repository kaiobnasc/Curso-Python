dias = int(input("Quantos dias alugados: "))
km = float(input("Quantos km's você rodou: "))
valordia = dias * 60
valorkm = km * 0.15
valorTotal = valordia + valorkm

print("O carro foi alugado por {} dias e rodou {} km's, no total deve ser pago R${:.2f}".format(dias, km, valorTotal))