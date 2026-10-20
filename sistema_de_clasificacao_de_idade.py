# Algoritmo "classifica_idade"
# Var
#// Seção de Declaração de Variáveis
#idade: inteiro

# Inicio
#    // Seção de Comandos
#escreval("Digite sua idade: ")
#leia(idade)
#se (idade >= 0) e (idade <= 12) entao
#       escreval("Você é uma criança")
#fimse
   
#se (idade >= 13) e (idade <= 17) entao
#       escreval("Você é um adolescente")
#fimse
   
#se (idade >= 18) e (idade <= 64) entao
#       escreval("Você é um adulto")
#fimse 
# se (idade >= 65) e (idade <=99) entao
#   escreval("O senhor(a) é um idoso")
#fimse
# se (idade >= 100) entao
#    escreval("Para de mentir macho")
#fimse
# Fimalgoritmo
import os
os.system('cls || clear')



print("Escreva a sua idade: ")
idade= int(input())
if (idade >= 0) and (idade <=12):
    print("Você é uma criança")
if (idade >= 13) and (idade <= 17):
    print("Você é um adolecente") 
if (idade >= 18) and (idade <= 64):
    print("Você é um adulto")
if (idade >= 65) and (idade >= 99):
    print("Você é um idoso")  
if (idade >= 100): 
    print("Para de mentir macho")           