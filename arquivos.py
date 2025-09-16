import json

def ler_arquivo():
    dados = []
    with open('jogadoras.json', 'r') as arq:
        dados = json.load(arq)
    return dados

def adicionar_arquivo(dados):
    with open('jogadoras.json', 'w') as arq:
        json.dump(dados, arq)