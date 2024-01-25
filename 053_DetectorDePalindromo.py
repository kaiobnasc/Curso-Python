frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #separa a frase em um vetor letra por letra
junto = ''.join(palavras) #junta as strings usando o que tiver entre ''
inverso = ''
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!') #print que imprime ume mensagfem
else:
    print('A frase digitada não é um palindromo!')
    print('Teste de print')
    print('Teste 2')