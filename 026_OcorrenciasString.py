frase = str(input("Digite uma frase: ")).upper().strip() #Variável recebe um string sem espaços no inicio e fim (strip()) e upper() transforma a string em maiúscula

print("A letra A aparece {} vezes na frase.".format(frase.count("A"))) #Conta quantas vezes a letra A aparece
print("A primeira letra A apareceu na posição {}.".format(frase.find("A"))) #Mostra em que posição a letra A apareceu pela primeira vez
print("A última letra A apareceu na posição {}.".format(frase.rfind("A"))) #Mostra em que posição a letra A apareceu pela última vez