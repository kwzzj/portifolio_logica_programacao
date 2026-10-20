import os
os.system("cls")

menor=0
maior=0
i=0
notas = [7, 8.5, 6, 9, 5.5] #cria a lista

quantidadeValores= len(notas) #le a quantidade de valores
indicePrimeirovalor= notas.index(7) #Procura o índice
ultimoindice= len(notas)-1 #procura o ultimo índice

i=0#inicializa o "i"
while i < len(notas): #estrutura while com condição parada
    print(notas[i])#mostra cada item da lista
    i += 1 #ao final soma o valor com 1
 
#identificar a qunatidade de notas na lista
print(f"Existem {len(notas)} notas na lista")

#Somar a lista inteira
print(f"a soma da lista inteira é {sum(notas)}")

#encontrar o maior valor da lista
for i in range(5):
    if (notas[i] > maior):
        maior = notas[i]   
print(f'o maior número é: {maior}')

#encontrar o menor valor da lista
for i in range(5):
    if (notas[i] < menor):
        menor = notas[i]   
print(f'o menor número é: {menor}')

