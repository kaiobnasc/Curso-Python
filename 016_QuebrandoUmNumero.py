from math import trunc #Importando a biblioteca math e a sua função para cálculo da porção inteira 

numero = float(input("Digite um número: ")) # Print que pede ao usuário um número

print("O número digitado foi {}, e sua porção inteira é {}".format(numero, trunc(numero))) # Print que informa ao usuário o valor digitado e sua porção inteira