n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1+n2)/2
print("Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}".format(n1, n2, media))

if  media <= 6:
    print("Aluno em recuperação.")
else:
    print("Aluno aprovado.")