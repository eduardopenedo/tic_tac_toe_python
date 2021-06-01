# cria tabuleiro com "-" dentro
def novo_tabuleiro():
    tabuleiro = list()

    for i in range(3):
        # Adiciona linha na matriz
        tabuleiro.append([])

        # Adiciona "-" nas linhas da matriz
        for x in range(3):
            tabuleiro[i].append("-")
    return tabuleiro

def mostra_tabuleiro(tabuleiro):
    for i in range(len(tabuleiro)):
        # Mostra a linha gerada
        print(" ".join(tabuleiro[i]))

def ganhou(tabuleiro):
    resposta = ()

    # vitória horizontal e vertical
    for i in range(3):
        if (tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][0] == tabuleiro[i][2]):
            resposta = (True, tabuleiro[i][0])
        if (tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[0][i] == tabuleiro[2][i]):
            resposta = (True, tabuleiro[i][i])

    # vitória diagonal

    if (tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[0][0] == tabuleiro[2][2]):
        resposta = (True, tabuleiro[0][0])
    elif (tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[0][0] == tabuleiro[2][0]):
        resposta = (True, tabuleiro[0][2])

    if resposta[1] != '-':
        return resposta
    else:
        return (False,)


def jogar():
    tabuleiro = novo_tabuleiro()

    mostra_tabuleiro(tabuleiro)

    # Enquanto houver espaços em branco ("-") o loop irá ocorrer
    while ("-" in tabuleiro[0]) or ("-" in tabuleiro[1]) or ("-" in tabuleiro[2]):
        # Jogada jogador 1
        jogada1 = input("Jogador 1 - Escolha uma posição [x,y]\n> ")

        x = int(jogada1[3]) - 1
        y = int(jogada1[1]) - 1

        tabuleiro[x][y] = "X"

        mostra_tabuleiro(tabuleiro)


        if (ganhou(tabuleiro)[0]):
            print(str(ganhou(tabuleiro)[1]) + "ganhou")
            break

        # Jogada jogador 2
        jogada2 = input("Jogador 2 - Escolha uma posição [x,y]\n> ")
        x = int(jogada2[3]) - 1
        y = int(jogada2[1]) - 1
        tabuleiro[x][y] = "O"

        mostra_tabuleiro(tabuleiro)

if __name__ == '__main__':
    jogando = True
    while jogando:
        jogar()
        continuarjogando = input("Deseja Jogar Novamente? [S/N]")
        if continuarjogando in ["N","n"]:
            jogando = False
    else:
        print("Saindo ...")