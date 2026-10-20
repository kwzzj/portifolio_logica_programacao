import os
os.system('cls || clear')

print("Quantos graus está fazendo agora?")
graus= int(input())
if graus <18:
    print("está frio")
elif graus >=18 and graus <= 25 :
        print("Está agradável") 
elif graus >25:
      print("Está calor")  