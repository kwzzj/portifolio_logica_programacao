import os
os.system("cls || clear")

score=int(input("Digite o seu score: "))
renda_mensal=float(input("Digte a sua renda mensal: "))
fiador=str(input("Você tem fiador? "))
if fiador == 'sim':
    score_fiador=float(input("Digite o score do seu fiador: "))
else:
    print("")    
emprestimo=float(input("E quanto o senhor(a) Gostaria de empréstimo? "))    
if (score> 600) and (renda_mensal >= 2500) or (score <= 600) and (score_fiador > 700) and (emprestimo < renda_mensal):
    print("Ok senhor(a), o seu empréstimo será realizado nas próximas 48 horas")
else:
    print("O senhor não pode fazer o empréstimo")