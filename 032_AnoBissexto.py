from datetime import date # Importação da função date da biblioteca datetime

ano = int(input("Que ano quer analisar? Coloque 0 para analistar o ano atual: ")) # Variável ano recebe uma string através do INPUT
if ano == 0: # Início do ciclo IF que verifica se o valor digitado e armazenado na variável ANO é igual a 0
    ano = date.today().year #Variável ano recebe a informação do ano da data atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # Segundo Ciclo iF que verifica se o ano É BISSEXTO
    print("O ano {} é BISSEXTO.".format(ano)) # Print que informa se o ano é bissexto
else: # Else caso a condição seja falsa
    print("O ano {} não é BISSEXTO.".format(ano)) # Print que informa que o ano NÁO É BISSEXTOS