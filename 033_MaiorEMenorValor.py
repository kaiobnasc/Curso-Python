a = int(input("Digite o primeiro valor: ")) #Print que pede o primeiro valor
b = int(input("Digite o segundo valor: ")) #Print que pede o segundo valor
c = int(input("Digite o terceiro valor: ")) #Print que pede o terceiro valor
# Verificando o menor
menor = a # Variável menor recebe o conteúdo da variável A
if b < a and b < c: #Primeiro if verificando se B é o menor
    menor = b #Caso B seja o menor, a variável menor recebe o valor de B
if  c < a and c < b: #Segundo IF que verifica se a variável C é a menor
    menor = c #Caso C seja a menor, a variaável menor recebe o valor de C
# Verificando o maior
maior = a #Variável maior recebe o conteudo da variável A
if b > a and b > c: # Primeiro ciclo IF que verifica se B é a maior variável
    maior = b #Caso B seja a maior, a variável maior receberá o valor de B
if c > a and c > b: # Segundo ciclo IF que verifica se C é maior variável
    maior = c # Caso C seja a maior, a variável maior recebera o valor de C
    
print("O menor valor digitado foi {}".format(menor)) # Print que informa o menor valor digitado
print("O maior valor digitado foi {}".format(maior)) # Print que informa o maior valor digitado