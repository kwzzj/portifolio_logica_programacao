import os
os.system('cls || clear')

teclado= int(((100*5)/100) + 5)
placamãe= int(((500*15)/100) + 100)
mouse= int(((200*5)/100)+5)

nome= str(input("Olá, digite seu nome para se logar "))
senha= int( input("Digite sua senha "))


print("Bem vindo a nossa loja on-line!", nome)
print("Temos os seguintes produtos")
print("Temos  teclado")
print("Temos placa-mãe")
print("E também temos mouses")
print("Qual você deseja comprar?")
resposta= input(" ").lower()
os.system('cls || clear')
if resposta == 'teclado':
    print("ok senhor(a)", end='')
    print("estamos com um desconto de 5 porcento no teclado,", end='')
    print("Então o seu teclado fica ", teclado, end='')
    print('$')
if resposta == 'placa-mãe':
    print("ok, senhor(a)", end='')
    print('estamos com um desconto alto na placa mãe.')
    print("A placa mãe sai por volta de ", placamãe, end='')
    print("$")    
if resposta == 'mouse':
    print("ok, senhor(a)")
    print("os nossos mouses estão com desconto")
    print("pra vc meu amigo, eu consigo fazer pra vc em ", end='')
    print("", mouse)
    print("$") 
    print("Já com o frete incluso")      

resposta2= input("Será no crédito; débito ou no dinheiro? ").lower()
os.system('cls || clear')
if resposta2== 'débito':
    print("ok, pode aporximar o cartão.")
    print("", nome, end='')
    print(" o cartão foi aprovado, tenha um bom dia.")
if resposta2== 'crédito':
    print("ok, pode aproximar o cartão. ")
    print("", nome, end='')
    print("  cartão foi aprovado. Tenha um bom dia.")
if resposta2== 'dinheiro':
    print("ok,", nome)
    print("tenha um bom dia")    