a = input("Digite algo: ") # Print pedindo para digitar algo

print("O tipo premitivo desse valor é: ", type(a)) # Print que verifica qual o tipo premitivo do valor digitado
print("Só tem espaços?", a.isspace()) # Print retorna se no valor digitado possui apenas espaços
print("É um número?", a.isnumeric()) # Print que retorna se o valor digitado é um número ou não
print("É alfabético?", a.isalpha()) # Print que retorna se o valor é alfabético ou não
print("É alfanumérico?", a.isalnum()) # Print que retorna se o vlaor é alfanumérico ou não
print("Está em maiúsculas?", a.isupper()) # Print que retorna se o valor digitado está em maíscula ou não
print("Está em minúsculas?", a.islower()) # Print que retorna se o valor digitado está em minúsculas ou não
print("Está capitalizada?", a.istitle()) # Print que retorna se o valor digitado está capitalizado ou não