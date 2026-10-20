import os
os.system('cls')
from tarefas import tarefas


while True:
    print("\n--- Lista de tarefas ---")
    print("1 - Adicionar tarefas")
    print("2 - Listar Tarefas")
    print("3 - Sair")
    opcao = int(input('Digite a opção que deseja'))

    if (opcao == 1):
        print('Opção para adicionar uma tarefa')
    
    elif (opcao == 2):
        print('Opção para listar as tarefas')
    elif (opcao == 3):
        print("Programa encerrado")
        break
    else:
        print("Número inválido")
