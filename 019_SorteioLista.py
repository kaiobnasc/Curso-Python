from random import choice # Importação da função RANDOM da biblioteca CHOICE

a1 = str(input("Primeiro aluno: ")) # Primeiro nome
a2 = str(input("Segundo aluno: ")) # Segundo nome
a3 = str(input("Terceiro aluno: ")) # Terceiro nome
a4 = str(input("Quarto aluno: ")) # Quarto nome
lista = [a1, a2, a3, a4] # Colocando todos os nomes dentro de uma lista de strings
escolhido = choice(lista) # A função CHOICE puxando a lista para escolha de um nome

print("O aluno sorteado foi {}".format(escolhido)) # Print para mostrar na tela qual nome da lista de strings foi sorteado.
