largura = float(input("Digite a largura da parede: ")) # Print que pede ao usuário uma informação
altura = float(input("Digite a altura da parede: ")) # Print que pede ao usuário uma informação
area = largura * altura # Variável area recebe o cálculo de largura x altura
tinta = area/2 # Variável tinta recebe o valor da area dividido por 2

print("Sua parede tem a dimensão {:.2f}x{:.2f} e sua área é de {:.2f}m².".format(largura, altura, area)) # Print das dimensões da parede e sua área
print("Para pintar essa parede, você precisará de {}l de tinta.".format(tinta)) # Print de quantos litros de tinta irá precisar.