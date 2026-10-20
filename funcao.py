import os
os.system('cls')

n1= int(input("Digite o primeiro número "))
sinal= str(input("Digite o sinal "))
n2= int(input("Digite o segundo número "))


if (sinal == '+'):
    print(f'{n1} + {n2} = {n1+n2}')
elif (sinal == '-'):    
    print(f'{n1} - {n2} = {n1-n2}')
elif (sinal == '*'):    
    print(f'{n1} * {n2} = {n1*n2}')
else:  
    print(f'{n1} /{n2} = {n1/n2}')