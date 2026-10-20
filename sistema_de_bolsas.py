import os
os.system('cls || clear')

atleta= True
nota= 8.5
renda= 1640
bolsa100= (nota>=9 and renda<=2000)

print("O aluno é elegivel para a bolsa de 100%:", bolsa100)

bolsa50= (nota>=8 and renda>=3000) or atleta

print("O aluno é elegivel para a bolsa de 50%:", bolsa50)