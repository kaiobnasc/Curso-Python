from random import randint
from time import sleep

numero = randint(0, 5)
print("-" * 20)
print("Vou pensar em um número entre 1 e 5. Tente adivinhar...")
print("-" * 20)
jogador = int(input("Número que eu pensei: "))
print("PROCESSANDO...")
sleep(2)
if numero == jogador:
    print("Parabéns você acertou, eu pensei no número {} e você também! VOCÊ GANHOU!".format(numero))
else:
    print("Você perdeu. Eu pensei no numero {} e você pensou no {}.".format(numero, jogador))