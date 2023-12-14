casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento: '))
prestacao = casa / (anos * 12)
minimo = salario * 30/100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print('A prestação será de R${:.2f}'.format(prestacao))

if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo negado.')
