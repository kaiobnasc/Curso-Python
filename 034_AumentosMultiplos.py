salario = float(input("Qual é o salário do funcionário: R$"))

if salario >= 1250:
    nsalario = salario + (salario * 10/100)
    print("O salário do funcionário é de R${:.2f} e com o aumento passou a ser R${:.2f}".format(salario, nsalario))
else:
    nsalario = salario + (salario * 15/100)
    print("O salário do funcionário é de R${:.2f} e com o aumento passou a ser de R${:.2f}".format(salario, nsalario))