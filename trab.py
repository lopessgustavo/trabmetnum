def zerarColuna(matriz,linha,matrizB):
    coluna = linha
    matrizB[linha][coluna] = 1
    for i in range(linha+1,len(matriz)):
        multiplicador = matriz[i][coluna]/matriz[linha][coluna]
        matrizB[i][coluna] = multiplicador
        #subtrair linhas
        for j in range(coluna,len(matriz)):
            matriz[i][j] -= matriz[linha][j]*multiplicador    

def imprime(matriz):
    for linha in matriz:
        print(linha)

def pivotear(matriz,coluna,mZeros):
    linha = coluna
    maior = coluna
    for i in range(linha, len(matriz)):
        if abs(matriz[i][coluna]) > matriz[maior][coluna]:
            maior = i
    matriz[linha], matriz[maior] = matriz[maior],matriz[linha]
    mZeros[linha], mZeros[maior] = mZeros[maior], mZeros[linha]

def matriz_de_zeros(tam):
    matriz = []
    for i in range(tam):
        linha = []
        for j in range(tam):
            linha.append(0)
        matriz.append(linha)
    return matriz

def eliminacaoGauss(matriz):
    # verificarDiagonalPrincipal(matriz)
    mZeros = matriz_de_zeros(len(matriz))
    for linha in range(len(matriz)):
        pivotear(matriz,linha,mZeros)
        zerarColuna(matriz,linha,mZeros)
    imprime(matriz)
    imprime(mZeros)


if __name__ == '__main__':
    matriz =    [[2,-1,4,0],
                [4,-1,5,1],
                [-2,2,-2,3],
                [0,3,-9,4]]
    eliminacaoGauss(matriz)
            