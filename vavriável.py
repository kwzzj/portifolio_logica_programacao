import os
os.system('cls || clear')

print("Registre-se")
email=input("digite seu email: ")
os.system('cls || clear')
senha=input("digite sua senha: ")
os.system('cls || clear')
número=input("digite seu número: ")
os.system('cls || clear')
print("só para confirmar seus dados", end='')
print("o seu email é: ", email)
print("digite seu número de telefone é: ", número)
print("está correto?")
resposta=input("(sim/não):").lower()
os.system('cls || clear')
if resposta =='sim':
    print("ok, seu cadastro foi concluido")
if resposta =='não':    
     print("senhor, peço que faça o cadastro mais uma vez, e desta vez tenha mais atenção na sua escrita!!")
if resposta =='s':
    print("senhor, tenha mais atenção na sua gramática!")
    print("refaça seu cadastro")
if resposta =='n': 
    print("senhor, peço que tenha mais atenção na sua gramática!", end='')
    print("refaça seu cadastro")
