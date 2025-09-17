from funcoes import *
import os

jogadoras = [
    {
        "nome": "Andressa Alves",
        "batimentos": 70,
        "desempenho": {  
            "distancia_percorrida_km": 10,
            "velocidade_media_kmh": 15
        },
        "estatisticas_gols": (28, 15)
    },
    {
        "nome": "Dayana Rodríguez",
        "batimentos": 68,
        "desempenho": {
            "distancia_percorrida_km": 5,
            "velocidade_media_kmh": 12
        },
        "estatisticas_gols": (30, 5)
    }
    ]

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
    elif opcao == "6":
        os.system("cls")
    elif opcao == "0":
        print("Encerrando... Obrigado por usar o Passa a Bola!")
        break
    else:
        print("Opção inválida, tente novamente.")