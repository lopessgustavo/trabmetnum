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
    matriz_l = matriz_de_zeros(len(matriz))
    for linha in range(len(matriz)):
        pivotear(matriz,linha,matriz_l)
        zerarColuna(matriz,linha,matriz_l)
    print("Matriz L")
    imprime(matriz_l)
    print("Matriz U")
    imprime(matriz)
    return matriz_l, matriz

def resolverSistema(matriz,vet_b):
    matriz_l, matriz_u = eliminacaoGauss(matriz)
    triangular_superior(matriz_l,vet_b)

def triangular_superior(matriz,vet):
    vet_resp = []
    for i in range(len(matriz)):
        soma = 0
        # print('oie')
        for j in range(i):
            soma += matriz[i][j]*vet_resp[j]
        print(soma)
        vet_resp.append(vet[i]-soma)
    print(vet_resp)

def triangular_inferior(matriz,vet):
    vet_resp = []
    for i in range(len(matriz)):
        soma = 0
        # print('oie')
        for j in range(i):
            soma += matriz[i][j]*vet_resp[j]
        print(soma)
        vet_resp.append(vet[i]-soma)

if __name__ == '__main__':
    # matriz =    [[2,-1,4,0],
    #             [4,-1,5,1],
    #             [-2,2,-2,3],
    #             [0,3,-9,4]]
    # eliminacaoGauss(matriz)
    matriz =    [[1,0,0],
                [2,1,0],
                [-1,0,1]]
                
    b = [2,-1,1]
    triangular_superior(matriz,b)