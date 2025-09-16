from funcoes import *
from arquivos import *

jogadoras = ler_arquivo()

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        ver_batimentos(jogadoras)
    elif opcao == "2":
        ver_desempenho(jogadoras)
    elif opcao == "3":
        ver_estatisticas_gols(jogadoras)
    elif opcao == "4":
        listar_jogadoras(jogadoras)
    elif opcao == "5":
        adicionar_jogadora(jogadoras)
    elif opcao == "0":
        print("Encerrando... Obrigado por usar o Passa a Bola!")
        break
    else:
        print("Opção inválida, tente novamente.")