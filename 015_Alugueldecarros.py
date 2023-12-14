dias = int(input("Quantos dias alugados: ")) # Print que pergunta ao usuário quantos dias ele alugou
km = float(input("Quantos km's você rodou: ")) # Print que pergunta ao usuário quantos km's ele rodou
valordia = dias * 60 # Variável valordia recebe o cálculo para contar verificar o valor pelos dias
valorkm = km * 0.15 # Variável valorkm recebe o cálculo para calcular o valor por km's rodados
valorTotal = valordia + valorkm # Cálculo para descobriro valor total

print("O carro foi alugado por {} dias e rodou {} km's, no total deve ser pago R${:.2f}".format(dias, km, valorTotal)) # Print que mostra na tela quantidade de dias alugados, quantos km's rodados e o valor a ser pago.