import os
os.system("cls")

m= [2,5,1,4] , [7,0,3,8] , [6,9,2,5]

NL = len(m)
NC = len(m[0])
TE = NL * NC
# print(f'A matriz tem {NL} linhas e {NC} colunas, possuindo {TE} elementos')
# LM = []
# for L in range (NL):
#     for C in range (NC):
#         print(m[L][C])
#         LM.append(m[L][C])
#         print(LM)
# print(f'A matriz em Row-Major fica dessa forma:\n {LM}')

# L = int(input('Em qual linha está o número que você deseja descobrir a nova posição na lista Row-major?: '))
# C = int(input('Em qual coluna está o número que você deseja descobrir a nova posição na lista Row-major?: '))

# offset = (L -1) * NC + (C -1)
# print(offset)

# for i, L in enumerate(m):
#     print(f'Soma da linha {i}: {sum(L)}')
#     #esse for funciona pois, o "enumarete" adiciona adiciona uma contagem a cada item de uma lista ou texto. Já o "sum" soma todos os números dentro de uma lista ou sequência. E para fazermos a soma das colunas é exatamente a mesma coisa, basta trocar as variáveis.
# for i, C in enumerate(m):
#     print(f'Soma das coluna {i}: {sum(C)}')