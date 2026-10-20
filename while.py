import os
os.system("cls")

# contador = 22

# while contador >= 8:
#     print(f"O contador está no {contador}º número")
#     contador += 1
#nesse caso o computador irá continuar a sequência até o final dos tempos, pois a nossa condição é que o seguinte
#Se o contador for maior ou igual a 8, então ele deve continuar. Como nós dizemos que o contador é = 22,
# então ele nunca vai parar de contar.
# contador =2
# while contador >= 8:
#     print(f"O contador está no {contador}º número")
#     contador += 1
#Porém nesse caso o programa nem começa
#pois como a nossa condição é >=8 e 2 é menor que 8,
while True:
    n=int(input("Digite um número "))
    if n %2 == 0:
        print("Vc colocou um número par")
        break
    else:
        print("Vc n colocou um número par")
        break
print("Fim")    