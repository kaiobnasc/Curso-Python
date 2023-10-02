import math

oposto = float(input("Digite o comprimento do cateto oposto: "))
adjacente = float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa = math.hypot(oposto, adjacente)


print("A hipotenusa do triangulo vai valer {:.2f}".format(hipotenusa))