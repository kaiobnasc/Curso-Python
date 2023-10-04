from math import hypot # Importação da biblioteca math e de sua função hypot

oposto = float(input("Digite o comprimento do cateto oposto: ")) # Print que pede ao usuário o comprimeiro do cateto oposto
adjacente = float(input("Digite o comprimento do cateto adjacente: ")) # Print que pede ao usuário seu cateto adjacente
hipotenusa = math.hypot(oposto, adjacente) # Variável hipotenusa recebe o cálculo usando a função hypot


print("A hipotenusa do triangulo vai valer {:.2f}".format(hipotenusa)) # Print que mostra na tela o valor da hipotenusa do triângulo