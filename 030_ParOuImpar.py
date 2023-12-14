numero = int(input("Digite um número qualquer: ")) #Variável numero recebe o input para que o usuário digite o número 
resultado = numero % 2 #Variável resultado recebe o cálculo

if resultado == 0: #Início do ciclo IF, onde ele compara a variável resultado se ela está com o valor 0
    print("O número {} é PAR.".format(numero)) # Print que informa ao usuário o valor se ele for par
else: # Segunda condição do ciclo if
    print("O número {} é ÍMPAR.".format(numero)) # Print que informa ao usuário o valor do número se ele for iMPAR