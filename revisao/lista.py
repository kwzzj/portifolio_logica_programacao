import os
os.system("cls")

lista=[1,2,3]
for j in range(3):
    print(f"A posição {j} da lista é: {lista[j]}")

media=sum(lista) / len(lista)
print(f"O valor da média é: {media}")
