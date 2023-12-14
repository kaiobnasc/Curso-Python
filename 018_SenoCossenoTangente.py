import math # Importação da biblioteca Math

angulo = float(input("Digite o ângulo que você deseja: ")) # Print que pede ao usuário que ele digite um ângulo
seno = math.sin(math.radians(angulo)) # Variável seno recebe o cálculo
cosseno = math.cos(math.radians(angulo)) # Variável cosseno recebe o cálculo
tangente = math.tan(math.radians(angulo)) # Variável tangente recebe o cálculo

print("O seno de {} é {:.2f}".format(angulo, seno)) # Print que mostra o ângulo e o seno do ângulo.
print("O cosseno de {} é {:.2f}".format(angulo, cosseno)) # Print que mostra o ângulo e o cosseno do ângulo.
print("O tangente de {} é {:.2f}".format(angulo, tangente)) # Print que mostra o ângulo e sua tangente.