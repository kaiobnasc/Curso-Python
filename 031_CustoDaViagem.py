distancia = float(input("Qual é a distância da sua viagem: ")) # Input que pede ao usuario que ele digite uma distancia que é armazenada em uma variável
print("Você está prestes a começar uma viagem de {} KM".format(distancia)) # Print que imprime uma string na tela
if distancia <= 200: # Começo do ciclo IF que compara para ver se a variável distancia é menor ou igual a 200
    preco = distancia * 0.50 # Cálculo realizado caso a primeira verificação do ciclo IF for verdadeira
    print("E o preço da sua viagem sera de R${:.2f}".format(preco)) # Print que informa o preço da viagem na tela
else: # Segunda parte do ciclo IF
    preco = distancia * 0.45 # Segundo cálculo caso a verficação do ciclo IF retorne um valor FALSO
    print("E o preço da sua viagem será de R${:.2f}".format(preco)) # Print que informa ao usuário o preço da viagem.