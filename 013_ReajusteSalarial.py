salario = float(input("Qual é o salário do funcionário?: R$")) # Print que pergunta qual o salário do funcionário
novo = salario + (salario * 15/100) # Variável novo recebe o cálculo do novo salário

print("Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}".format(salario, novo)) # Print mostra o antigo salário e o novo após o reajuste