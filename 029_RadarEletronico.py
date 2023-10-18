velocidade = int(input("Qual é a velocidade do carro: ")) # Input que pede ao usuário que responde qual a velocidade do carro

if velocidade < 80: # Inicio de um ciclo if que compara se a variável velocidade contém valor menor que 80
    print("Tenha um bom dia, dirija com cuidado!") # Print de uma mensagem na tela
else: # Segunda parte da condição if
    multa = (velocidade - 80) * 7 # Variável recebe o cálculo para informação da multa
    print("Você está acima do permitido. Sua velocidade é {} e sua multa é de R${}".format(velocidade, multa)) # Print que informa na tela  a velocidade e o valor da multa