import os
os.system("cls || clear")

print("digite o valor total")
total= float(input())
if (total > 100) and (total < 500):
    print("você ganhou 5% de desconto", total * 0.5)
if (total > 500):
    print("Você ganhou 10% de desconto", total * 0.10)
if (total > 200) and (total < 500):
    print("Você possui um frete de 15$")        