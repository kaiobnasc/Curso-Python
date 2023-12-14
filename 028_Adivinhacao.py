from random import randint #Importa a função randint da biblioteca random
from time import sleep #Importa a função sleep da biblioteca time

numero = randint(0, 5) # Variável inteira numero recebe um numero aleatório entre 1 e 5 através da funçõa randint
print("-" * 20) # Printa na tela 20x o traço
print("Vou pensar em um número entre 1 e 5. Tente adivinhar...") # Printa mensagem na tela
print("-" * 20) # Printa na tela 20x o traço
jogador = int(input("Número que eu pensei: ")) # Input que pede ao usuário um número que é armazenado na variável jogador
print("PROCESSANDO...") # Printa mensagem na tela
sleep(2) # Uso da função sleep onde o terminal ˜dorme˜ pelos segundos indicados entre parênteses
if numero == jogador: #Início do ciclo if que compara se o valor contído na variável numero é igual ao valor contído na variável jogador
    print("Parabéns você acertou, eu pensei no número {} e você também! VOCÊ GANHOU!".format(numero)) # Printa mensagem na tela caso a condição seja verdadeira
else: # Início da segunda condição do ciclo if
    print("Você perdeu. Eu pensei no numero {} e você pensou no {}.".format(numero, jogador)) # Printa mensagem na tela caso a condição seja falsa