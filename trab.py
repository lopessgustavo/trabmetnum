def zerarColuna(matriz,linha):
    coluna = linha
    for i in range(linha+1,len(matriz)):
        multiplicador = matriz[i][coluna]/matriz[linha][coluna]
        
        #subtrair linhas
        for j in range(coluna,len(matriz)):
            matriz[i][j] -= matriz[linha][j]*multiplicador

def imprime(matriz):
    for linha in matriz:
        print(linha)

def pivotear(matriz,coluna):
    linha = coluna
    maior = coluna
    for i in range(linha, len(matriz)):
        if abs(matriz[i][coluna]) > matriz[maior][coluna]:
            maior = i
    matriz[linha], matriz[maior] = matriz[maior],matriz[linha]


def eliminacaoGauss(matriz):
    # verificarDiagonalPrincipal(matriz)
    
    for linha in range(len(matriz)):
        pivotear(matriz,linha)
        zerarColuna(matriz,linha)

if __name__ == '__main__':
    matriz =    [[2,-1,4,0],
                [4,-1,5,1],
                [-2,2,-2,3],
                [0,3,-9,4]]
    eliminacaoGauss(matriz)
    imprime(matriz)
    # tam = int(input())
    # matriz = []W
    # for i in range(tam):
    #     linha =         
            