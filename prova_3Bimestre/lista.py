import os
os.system("cls")

numeros = [12, 5, 8, 21, 7, 30, 14, 9]

#mostar os números
for j in range(8):
    print(numeros[j])
#soma deles
soma=sum(numeros)
print(f"O total da soma é: {soma}")
#Quantos sao pares
for j in range(8):
    if (j%2 ==0):
        print(f"O número {j} é par")
else:
    print(f"O número {j} é impar")    

