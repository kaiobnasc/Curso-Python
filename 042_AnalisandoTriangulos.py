print("-" * 20) #Print que imprime um traço 20x na tela
print("Analisador de triângulos") #Print que imprime string
print("-" * 20) #Print que imprime um traço 20x na tela
r1 = float(input("Primeiro segmento: ")) #Input que pede ao usuário o primeiro segmento
r2 = float(input("Segundo segmento: ")) #Input que pede ao usu;ario o segundo segmento
r3 = float(input("Terceiro segmento: ")) #Input que pede ao usuário o terceiro segmento

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: #Incio do ciclo if que verifica se cada lado é menor que a soma dos outros dois lados
    print("Os segmentos PODEM formar um triângulo ", end="") #Print caso a condição anterior seja verdadeira
    if r1 == r2 == r3:
        print("Equilátero!")
    if r1 != r2 != r3 != r1:
        print("Escaleno.")
    else:
        print("Isósceles.")
else:
    print("Os segmentos acima NÃO podem formar um triângulo.")