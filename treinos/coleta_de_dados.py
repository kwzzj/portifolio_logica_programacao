import os
os.system('cls || clear')

senha= float =  0.0
nome= str=""
salario= int=0.0
nacionalidade= str="brasileiro"

senha = int = input("Digite uma senha apenas com números: ")
os.system('cls || clear')
nome =input("Digite seu nome: ")
os.system('cls || clear')
idade= int= input("Digite sua idade: ")
os.system('cls || clear')
salario = float=input("Digite seu salário: ")
os.system('cls || clear')
nacionalidade = input("Você sua nacionalidade é: ")
os.system('cls || clear')

print("O seu nome é", nome, end='')
print("?")

resposta1 = input("(s/n): ").lower()

if resposta1 == 'sim':
    print("ok, ")
elif resposta1 == 'não':
    input("Então qual é? ")
else:
    print("Resposta inválida.")
if resposta1== 's':
    print("ok, ")
if resposta1== 'n':
    print("Então qual é? ")   
   
print("sua idade é: ", idade)

resposta2 = input("(sim/não): ").lower()

if resposta2 == 'sim':
    print("ok, ")
elif resposta2 == 'não':
    print("Então qual é? ")
else:
    print("Resposta inválida.")

    resposta2 = input("(s/n): ").lower()

if resposta2 == 's':
    print("ok, ")
elif resposta2 == 'n':
    input("Então qual é? ")
else:
    print("Resposta inválida.")
if resposta2== 's':
    print("ok, ")
if resposta2== 'n':
    input("Então qual é? ")   


    
resposta3 = input("(sim/não): ").lower()

if resposta3 == 'sim':
    print("ok, ")
elif resposta3 == 'não':
    input("Então qual é? ")
else:
    print("Resposta inválida.")
if resposta3== 's':
    print("ok, ")
elif resposta3== 'n':
    input("Então qual é? ")   




os.system('cls || clear')

os.system('cls || clear')
print("Seu salário é: ", salario, end='')
print("?")

resposta = input("(sim/não): ").lower()

if resposta == 'sim':
    print("ok, ")
elif resposta == 'não':
    input("Então qual é? ")
else:
    print("Resposta inválida.")

os.system('cls || clear')

print("Sua senha é", senha)

resposta = input("(sim/não): ").lower()

if resposta == 'sim':
    print("ok, ")
elif resposta == 'não':
    input("Então qual é? ")
else:
    print("Resposta inválida.")
os.system('cls || clear')

print("E por fim, a sua nacionalidade é", nacionalidade,)

resposta = input("(sim/não): ").lower()

if resposta == 'sim':
    print("ok, ")
elif resposta == 'não':
    input("Então qual é? ")
else:
    print("Resposta inválida.")