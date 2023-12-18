peso = float(input("Digite seu peso (kg):"))
altura = float(input("Digite sua altura (m): "))
imc = peso/(altura**2)

print("O IMC dessa pessoa é {:.1f}".format(imc))

if imc < 18.5:
    print("Você está abaixo do seu peso normal.")
elif 18.5 < imc < 25:
    print("Você está no seu peso ideal.")
elif 25 < imc < 30:
    print("Você está em sobrepeso")
elif 30 < imc < 40:
    print("Você está em obesidade.")
else:
    print("Você está em obesidade mórbida")