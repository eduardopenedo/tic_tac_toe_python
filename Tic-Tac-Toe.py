# Cria tabuleiro com "-" dentro
# null -> list
def novo_tabuleiro():
    tabuleiro = list()

    for i in range(3):
        # Adiciona linha na matriz
        tabuleiro.append([])

        # Adiciona "-" nas linhas da matriz
        for x in range(3):
            tabuleiro[i].append("-")
    return tabuleiro

# Mostra o tabuleiro
# null -> null
def mostra_tabuleiro(tabuleiro):
    for i in range(len(tabuleiro)):
        # Mostra a linha gerada
        print(" ".join(tabuleiro[i]))

# Verifica se há uma situação de vitória, retornando True quando há e False quando não há
# list -> tuple
def ganhou(tabuleiro):
    resposta = (False,"-")

    # vitória horizontal e vertical
    for i in range(3):
        # horizontal
        if (tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][0] == tabuleiro[i][2]):
            resposta = (True, tabuleiro[i][0])
        # vertical
        if (tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[0][i] == tabuleiro[2][i]):
            resposta = (True, tabuleiro[0][i])

    # vitória diagonal

    if (tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[0][0] == tabuleiro[2][2]):
        resposta = (True, tabuleiro[0][0])
    elif (tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[0][0] == tabuleiro[2][0]):
        resposta = (True, tabuleiro[0][2])

    if resposta[1] != '-':
        return resposta
    else:
        return (False,"-")

# Se há espaços em branco ("-") na matriz retorna True, caso contrário, retorna False
# list -> bool
def espaco_em_branco(tabuleiro):
    ha_espaco = False
    for i in range(3):
        if "-" in tabuleiro[i]:
            ha_espaco = True
    return ha_espaco

# Verifica se critérios que a jogada deve possuir
# string, list -> bool
def jogada_valida(jogada,tabuleiro):
    valida = False
    len_colunas = len(tabuleiro)
    len_linhas = len(tabuleiro[0])
    if len(jogada)==5 and jogada[0] == "[" and jogada[2] == "," and jogada[4] == "]":
        x = int(jogada[1]) - 1
        y = int(jogada[3]) - 1
        if x<=len_linhas and y<=len_colunas and tabuleiro[y][x] == "-":
            valida = True
    return valida

# Realiza a jogada pretendida
# int, list, string -> null
def realizar_jogada(numero_jogador, tabuleiro, marcador):
    # Pede jogada a ser feita
    jogada = input(str.format("\nJogador {} - Escolha uma posição [x,y]\n> ", numero_jogador))

    # Enquanto a jogada não for validada, pede outra entrada
    while jogada_valida(jogada,tabuleiro) == False:
        print("\nJogada inválida. Tente novamente ... \n")
        jogada = input(str.format("\nJogador {} - Escolha uma posição [x,y]\n> ", numero_jogador))

    # executa a jogada
    x = int(jogada[1]) - 1      # considera que usuário irá fornecer entradas entre 1-3 e não de 0-2
    y = int(jogada[3]) - 1      # considera que usuário irá fornecer entradas entre 1-3 e não de 0-2
    tabuleiro[y][x] = marcador

# inica um novo jogo
# null -> null
def jogar():
    # Inicia novo tabuleiro
    tabuleiro = novo_tabuleiro()

    # Mostra tabuleiro
    mostra_tabuleiro(tabuleiro)

    # Enquanto houver espaços em branco ("-") o loop irá ocorrer
    while (espaco_em_branco(tabuleiro)):

        # Jogada jogador 1
        realizar_jogada(1, tabuleiro, "X")

        # Mostra o tabuleiro após a jogada
        mostra_tabuleiro(tabuleiro)

        # Verifica se ganhou
        if (ganhou(tabuleiro)[0]):
            print("\n" + str(ganhou(tabuleiro)[1]) + " ganhou")
            break

        # Jogada jogador 2
        realizar_jogada(2, tabuleiro, "O")

        # Mostra o tabuleiro após a jogada
        mostra_tabuleiro(tabuleiro)

        # Verifica se ganhou
        if (ganhou(tabuleiro)[0]):
            print("\n" + str(ganhou(tabuleiro)[1]) + " ganhou")
            break

    # Verifica se deu velha 
    if espaco_em_branco(tabuleiro)==False and ganhou()==False:
        print("Velha!")

def main():
    jogando = True
    while jogando:
        # incia um novo jogo
        jogar()

        # Enquanto a resposta ao diálogo for diferente de "n" e "N" continua iniciando um novo jogo
        continuarjogando = input("Deseja Jogar Novamente? S/N\n> ")
        if continuarjogando in ["N", "n"]:
            jogando = False
            print("Saindo ...")

if __name__ == '__main__':
    main()