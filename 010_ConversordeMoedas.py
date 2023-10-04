valor = float(input("Quanto de dinheiro você tem na carteira: R$")) # Print que demanda ao usuário quanto  de dinheiro ele possui na carteira
conversor = valor/3.27 # Variável conversor recebe o cálculo de conversão

print("Com R${:.2f} você pode comprar U${:.2f}".format(valor, conversor))  # Print que retorna para o usuário o valor original e sua conversão