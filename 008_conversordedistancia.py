m = float(input("Digite uma distância em metros: ")) # Print que demanda um distância em metros para o usuário
cm = m * 100 # Variável recebe o cálculo para informar a distância em centímetros
mm = m * 1000 # Variável recebe o cálculo para informar a distância em milímetros

print("A medida de {}m corresponde a {:.2f}cm e {:.2f}mm.".format(m, cm, mm)) # Print que informa a medida em metros, centímetros e milímetros. 