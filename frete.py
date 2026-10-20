import os
os.system("cls || clear")

tipo_frete: str

print("Digite o peso do pacote")
peso=float(input())
if (peso > 10):
    print("O seu frete é o expresso")
elif (peso >2):
    print("O seu frete é o econômico")
else:
    print("Digite o seu frete")
    tipo_frete=str(input())        