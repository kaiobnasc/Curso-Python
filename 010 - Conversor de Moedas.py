valor = float(input("Quanto de dinheiro você tem na carteira: R$"))
conversor = valor/3.27

print("Com R${:.2f} você pode comprar U${:.2f}".format(valor, conversor))