import os
os.system('cls || clear')

i= int(input("Digite a sua idade: "))
p= float(input("Digite o seu peso: "))
if (i >=18) and (i<=69) and (p>50):
    print("Você pode doar sangue")
else:
    print("Você não pode doar sangue")    
