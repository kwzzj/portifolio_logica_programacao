import os
os.system("cls")

maior=0
menor=0
soma=0
i=0
temperaturas = [22, 25, 21, 24, 26, 23, 22]

while i < len(temperaturas):
    print(temperaturas[i])
    i += 1
    
while i < len(temperaturas):
    soma = soma + temperaturas[i]
    i += 1

media = soma / len(temperaturas)

procurada = 24
encontrou = False
i = 0

while i < len(temperaturas):
    if temperaturas[i] == procurada:
        encontrou = True
    i += 1
for i in range(len(temperaturas)):
    if (temperaturas[i] > maior):
        maior = temperaturas[i]  
print(f'a maior temperatura é: {maior}') 

for i in range(len(temperaturas)):
    if (temperaturas[i] < menor):
        menor = temperaturas[i]  
print(f'a menor temperatura é: {menor}')
