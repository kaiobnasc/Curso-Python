from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0
while opcao != 5:
    print('''  
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opcao = int(input('Qual é a sua opção?: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} e {} é igual a {}'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('A multipliação entre {} e {} é igual a {}'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            print('O valor {} é maior que {}'.format(n1, n2))
        else:
            print('{} é maior que {}'.format(n2, n1))
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente.')
    print('-=-'*10)
    sleep(2)
print('Fim do programa! Volte sempre!')
