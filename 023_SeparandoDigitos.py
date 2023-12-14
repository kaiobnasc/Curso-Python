num = int(input("Informe um número: "))
u = num // 1 % 10 # Divisão inteira por 1, pegando o numero, divide por 10 e pega o resto da divisão (módulo de 10)
d = num // 10 % 10 # Divisão inteira por 10, pegando o número, divide por 10 e pega o resto da divisão (módulo de 10)
c = num // 100 % 10 # Divisão inteira por 100, pegando o número, divide por 10 e pega o resto da divisão (módulo de 10)
m = num // 1000 % 10 # Divisão inteira por 1000, pegando o número, divide por 10 e pega o resto da divisão (módulo de 10)

print("Analisando o numero {}".format(num)) # Print que imprime da tela o numero analisado
print("Unidade: {}".format(u)) # Print que imprime na tela a unidade do número
print("Dezena: {}".format(d)) # Print que imprime na tela a dezena do número
print("Centena: {}".format(c)) # Print que imprime na tela a centena do número
print("Milhar: {}".format(m)) # Print que imprime na tela a milha do número