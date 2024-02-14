somaIdade = 0
mediaIdade = 0
maiorIdade = 0
nomeVelho = ''
totmulher20 = 0

for p in range(1,5):
    print(f'-------- {p} PESSOA ------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdade = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdade:
        maiorIdade = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaIdade = somaIdade/4
print(f'A média de idade do grupo é de {mediaIdade} anos.')
print('O homem mais velho tem {} anos e se chama {}.'.format(maiorIdade, nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))