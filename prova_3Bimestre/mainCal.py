import os
os.system("cls")
import calculadora


opcao= input("Digite o número de qual das opções abaixo deseja executar:")
while opcao == 5:
    print("1-soma")
    print("2-subtração")
    print("3-multiplicação")
    print("4-divisão")
    print("5-sair")
if opcao == 1:
    n1=input("Digite o primeiro número ")
    n2=input("Digite o segundo número ")
    sum(n1,n2)
    