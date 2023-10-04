from random import shuffle # Importação da função RANDOM da biblioteca SHUFFLE

n1 = str(input("Digite o primeiro nome: ")) # Digitando o primeiro nome
n2 = str(input("Digite o segundo nome: ")) # Digitando o segundo nome
n3 = str(input("Digite o terceiro nome: ")) # Digitando o terceiro nome
n4 = str(input("Digite o quarto nome: ")) # Digitando o quarto nome
lista = [n1, n2, n3, n4] # Jogando todos os nomes dentro de uma lista de caracteres
shuffle(lista) # Fazendo a desordenação das informações contidas dentro da lista de caracteres usando a função SHUFFLE

print("A ordem da lista é: {}".format(lista)) # Imprimindo na tela a lista desordenada.