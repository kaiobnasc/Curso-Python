n = str(input("Digite seu nome completo: ")).strip() # Armazena na variável n a string demandada sem espaços no início e fim.
nome = n.split() #Divide cada string e coloca em um vetor de strings
print(nome) #Printa o conteúdo da variável nome (printará o vetor com as strings separadas por posições)
print("Muito prazer em te conhecer.") # Print de uma string
print("Seu primeiro nome é {}".format(nome[0])) # Print do primeiro nome sendo buscado no vetor na primeira posição
print("Seu ultimo nome é {}".format(nome[len(nome)-1])) # Print do ultimo nome sendo buscado no tamanho do vetor -1 para pegar a ultima informação do vetor.