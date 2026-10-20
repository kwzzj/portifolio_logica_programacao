import os
os.system("cls")

n= int(input("Digite sua nota: "))
if n >= 7:
    print("Você está aprovado.")
elif n <=6.9 and n >=5:
    print("Você está de recuperação")    
else:
    print("Você foi reporvado")