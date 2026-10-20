import os
os.system("cls || clear")

int=batata= 10
int=maçã=5
int=banana=5

print("senhor, o que você pegou?", end='')
print(" Digite as coisas que comprou")
print("Escolha entre batata; maçã ou banana")
print("SIGA A ORDEM PRÉ DEFINIDA.")

resposta= input("").lower()
if resposta == 'batata':
    print("ok, a batata está ", batata)
    print("$")
if resposta == 'maçã':
    print("ok, a maça está ", maçã, end='')
    print("$")
if resposta == 'maçã e banana':
    print("ok, a maçã mais a banana fica ", banana + maçã, end='')
    print("$")
if resposta == 'maçã e batata':
    print("ok, a maçã mais a batata fica ", maçã + batata, end='')
    print("$")
if resposta == 'maçã, batata e banana':
    print("ok, a maçã mais a batata mais a banana fica ", maçã + batata + banana, end='')
    print("$") 


if resposta == 'banana':
    print("ok, a banana está ", banana, end='')
    print("$")   
if resposta == 'banana e batata':
    print("ok, a banana mais a batata fica ", banana + batata, end='')
    print("$")
if resposta == 'banana e maçã, batata':
    print("ok, a banana mais a maçã mais a batata fica ", banana + maçã + batata, end='')
    print("$")
if resposta == 'batata':    
    print("ok, a batata está ", batata, end='')
    print("$")
if resposta == 'batata e maçã':
    print("ok, a batata mais a maçã fica ", batata + banana, end='')
    print("$")
if resposta == 'batata, maçã e banana':
    print("ok, a batata mais a maçã mais a banana fica ", batata + maçã + banana, end='')
    print("$")
if resposta == 'batata e banana':
    print("ok, a batata mais a banana fica ", batata + banana, end='')    
    print("$")
else :
  print("Siga a ordem das palavras pré definidas.", end='')
  print(" A ordem é maçã, batata e banana. refaça as compras senhor(a)")