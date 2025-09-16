def mostrar_menu():
    print("\nMenu Estatísticas Futebol Feminino")
    print("1 - Ver batimento cardíaco de uma jogadora")
    print("2 - Ver desempenho em campo de uma jogadora")
    print("3 - Ver estatísticas de gols de uma jogadora")
    print("4 - Listar todas as jogadoras")
    print("0 - Sair")

def escolher_jogadora(jogadoras):
    print("\nEscolha a jogadora:")
    for i, jogadora in enumerate(jogadoras):
        print(f"{i+1} - {jogadora['nome']}")
    try:
        escolha = int(input("Digite o número da jogadora: "))
        if 1 <= escolha <= len(jogadoras):
            return jogadoras[escolha-1]
        else:
            print("Jogadora inválida!")
            return None
    except ValueError:
        print("Entrada inválida! Digite um número.")
        return None

def ver_batimentos(jogadoras):
    jogadora = escolher_jogadora(jogadoras)
    if jogadora:
        print(f"Batimentos cardíacos de {jogadora['nome']}: {jogadora['batimentos']} bpm")

def ver_desempenho(jogadoras):
    jogadora = escolher_jogadora(jogadoras)
    if jogadora:
        desempenho = jogadora["desempenho"]
        print(f"Desempenho de {jogadora['nome']}:")
        print(f" - Distância percorrida: {desempenho['distancia_percorrida_km']} km")
        print(f" - Velocidade média: {desempenho['velocidade_media_kmh']} km/h")

def ver_estatisticas_gols(jogadoras):
    jogadora = escolher_jogadora(jogadoras)
    if jogadora:
        jogos, gols = jogadora["estatisticas_gols"]
        if jogos is not None and gols is not None:
            media = gols / jogos if jogos > 0 else 0
            print(f"{jogadora['nome']} fez {gols} gols em {jogos} jogos.")
            print(f"Média de gols por jogo: {media:.2f}")
        else:
            print("Estatísticas de gols não cadastradas.")

def listar_jogadoras(jogadoras):
    print("\n--- Lista de Jogadoras ---")
    for jogadora in jogadoras:
        print(f"- {jogadora['nome']}")