import os
os.system('cls || clear')


resultado1= int()
resultado2= int()
resultado3= int()
resultado4= int()

numero1= int()
numero2= int()
numero3= int()
numero4= int()
numero5= int()







print("digite o 1º número")
numero1 = int(input())
print("digite o 2º número ")
numero2= int(input())
resultado1 = numero1 + numero2
print("O seu resultado deu ", end='')
print(resultado1)

print("agora escolha um númeoro para ser subtraído de seu resultado")
numero3 = int(input())
resultado2 = resultado1-numero3
print("O seu resultado deu ", end='')
print(resultado2)

print("agora, digite um número para ser dividido pelo seu resultado ")
numero4 = int(input())
resultado3 = resultado2/numero4
print("O seu resultado deu ", end='')
print(resultado3)

print("e agora, escolha um número para ser multiplicado ")
numero5 = int(input())
resultado4 = resultado3*numero5
print(resultado4)