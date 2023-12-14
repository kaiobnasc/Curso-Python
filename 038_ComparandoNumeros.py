num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

if num1 > num2:
    print("O número {} é maior que {}".format(num1, num2))
elif num2 > num1:
    print("O número {} é maior que {}".format(num2, num2))
else:
    print("Os número são iguais.")    