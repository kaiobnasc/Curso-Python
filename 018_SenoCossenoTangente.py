import math

angulo = float(input("Digite o ângulo que você deseja: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo)) 

print("O seno de {} é {:.2f}".format(angulo, seno))
print("O cosseno de {} é {:.2f}".format(angulo, cosseno))
print("O tangente de {} é {:.2f}".format(angulo, tangente))