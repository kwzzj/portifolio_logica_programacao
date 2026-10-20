import os
os.system('cls || clear')


print("Digite sua idade ")
numero=float(input())
if numero < 16:
    print("Não pode entrar")
elif numero >=16 and numero <18:
    print("Pode entrar com os pais")    
if numero >=18:
    print("Pode entrar")    
