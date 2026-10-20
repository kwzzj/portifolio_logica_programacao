import os
os.system('cls || clear')

nota1= float(input("Digite a primeira nota "))
nota2= float(input("Digite a segunda nota "))
media= (nota1+nota2)/ 2
if media>= 6:
    print("Você passou, a sua nota foi ", media)
else:
    print("Você foi reprovado")    