#Pergunta qual o nome já excluido os espaços ANTES E DEPOIS DA DIGITAÇÃO
nome = str(input("Digite seu nome completo: ")).strip() 
#Imprime o print
print("Analisando seu nome...") 
#Coloca a informação da variável 'nome' em maiúsculo
print("Seu nome em maiúscula é {}".format(nome.upper())) 
#Coloca a informação da variável 'nome' em minúsculo
print("Seu nome em minúscula é {}".format(nome.lower())) 
#Faz a subtração de quantas letras tem a variável nome, menos o a quantidade de espaços
print("Seu nome ao todo tem {} letras.".format(len(nome) - nome.count(" "))) 
#Indica qual o primeiro nome e o tamanho do primeiro nome
print("Seu primeiro nome é {} e ele tem {} letras.".format(nome.split()[0], len(nome.split()[0]))) 
