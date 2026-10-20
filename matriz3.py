import os
os.system("cls")

matriz = [[2,5,1,4],
          [7,0,3,8],
          [6,9,2,5]]

acumulador = 0
for coluna in range(0,4):
  acumulador = acumulador + matriz[0][coluna]