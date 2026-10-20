import os
os.system('cls')

def ler_vetor():
    nums = [] #Cria uma lista vazia chamada 'nums'
    n = int(input("Quantos números? ")) #armazena em 'n' quantos números existirão na lista
    for i in range(n): #For vai rodar a quantidade de números que a lista terá
        valor = int(input("Digite um número: ")) # Armazena em 'valor' o número digitado
        nums.append(valor) # Adiciona o número dito pelo usuário na lista nums
    return nums

def exibir_vetor(nums):
    print("Vetor:", nums) #Mostra a lista nums

def somar_vetor(nums):
    soma = 0
    for v in nums:
        soma += v
    return soma


def calcular_media_vetor(nums):
    soma = somar_vetor(nums)
    media = soma / len(nums)
    return media

def encontrar_maior_valor(nums):
    maior = nums[0]
    for v in nums:
        if v > maior:
            maior = v
    return maior

# Teste leitura de dados
vetor_numero = ler_vetor()

# Teste exibição do vetor
exibir_vetor(vetor_numero)

# Teste soma
resultado_soma = somar_vetor(vetor_numero)

print(f'O valor da soma: {resultado_soma}')

# Calcular a média
resultado_media = calcular_media_vetor(vetor_numero)

print(f'O valor da média é: {resultado_media}')

# Encontrar o maior valor

maior_valor = encontrar_maior_valor(vetor_numero)

print(f'O maior valor é: {maior_valor}')