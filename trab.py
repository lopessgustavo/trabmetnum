def zerarColuna(matriz,linha):
    coluna = linha
    for i in range(linha+1,len(matriz)):
        multiplicador = matriz[i][coluna]/matriz[linha][coluna]
        
        #subtrair linhas
        for j in range(coluna,len(matriz)):
            matriz[i][j] -= matriz[linha][coluna]*multiplicador


def eliminacaoGauss(matriz):
    # verificarDiagonalPrincipal(matriz)
    
    for linha in range(len(matriz)):
        zerarColuna(matriz,linha)

if __name__ == '__main__':
    linha,coluna = [int(x) for x in input().split(" ")]
    matriz = []
    for i in range(linha):
        linha = []
        
            