preço = float(input("Qual é o preço do produto: R$")) # Print que pergunta qual o preço do produto
novo = preço - (preço*5/100) # Variável novo recebe o cálculo do novo produto

print("O produto que custava R${} na promoção com desconto de 5% vai custar R${}".format(preço, novo)) # Print que mostra na tela o preço original do produto e seu preço com desconto