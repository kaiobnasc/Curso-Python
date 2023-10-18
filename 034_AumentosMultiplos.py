salario = float(input("Qual é o salário do funcionário: R$")) #Variável salário recebe o input que pergunta ao usuário qual o salário

if salario >= 1250: #Inicio do ciclo IF que verifica se o salário digitado foi maior ou igual a 1250
    nsalario = salario + (salario * 10/100) # Caso seja verdadeiro, nsalario recebe o cálculo para o novo salário
    print("O salário do funcionário é de R${:.2f} e com o aumento passou a ser R${:.2f}".format(salario, nsalario)) # Print que informa o salário e o novo salário com aumento
else: #Segunda parte do ciclo IF caso a condição seja negativa
    nsalario = salario + (salario * 15/100) # Caso seja falso, nsalario recebe o cálculo para o novo salário
    print("O salário do funcionário é de R${:.2f} e com o aumento passou a ser de R${:.2f}".format(salario, nsalario)) # Print que informa o antigo e o novo salário do funcionário.