import os
os.system('cls')

n1= int(input("Digite o primeiro número "))
sinal= str(input("Digite o sinal "))
n2= int(input("Digite o segundo número "))

#Criação de funções para cada operações
def soma():
    print(f'{n1} + {n2} = {n1+n2}')
def subtracao():
    print(f'{n1} - {n2} = {n1-n2}')
def multiplicacao():
    print(f'{n1} * {n2} = {n1*n2}')
def divisao():
    print(f'{n1} / {n2} = {n1/n2}')

if (sinal == '+'):
    soma()
if (sinal == '-'):
    subtracao()
if (sinal == '*'):
    multiplicacao()
if (sinal == '/'):
    divisao()


if (sinal == '+'):
    print(f'{n1} + {n2} = {n1+n2}')
elif (sinal == '-'):    
    print(f'{n1} - {n2} = {n1-n2}')
elif (sinal == '*'):    
    print(f'{n1} * {n2} = {n1*n2}')
else:  
    print(f'{n1} /{n2} = {n1/n2}')

