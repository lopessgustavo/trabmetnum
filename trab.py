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

def pivotear(matriz,coluna,mZeros,mIdentidade):
    linha = coluna
    maior = coluna
    for i in range(linha, len(matriz)):
        if abs(matriz[i][coluna]) > matriz[maior][coluna]:
            maior = i
    matriz[linha], matriz[maior] = matriz[maior],matriz[linha]
    mZeros[linha], mZeros[maior] = mZeros[maior], mZeros[linha]
    mIdentidade[linha], mIdentidade[maior] = mIdentidade[maior], mIdentidade[linha]

def matriz_de_zeros(tam):
    matriz = []
    for i in range(tam):
        linha = []
        for j in range(tam):
            linha.append(0)
        matriz.append(linha)
    return matriz

def matrizIdentidade(tam):
    matriz = matriz_de_zeros(tam)
    for i in range(tam):
        matriz[i][i] = 1
    return matriz


def decompor(matriz):
    matriz_l = matriz_de_zeros(len(matriz))
    matriz_p = matrizIdentidade(len(matriz))
    for linha in range(len(matriz)):
        pivotear(matriz,linha,matriz_l,matriz_p)
        zerarColuna(matriz,linha,matriz_l)
    print("Matriz L")
    imprime(matriz_l)
    print("Matriz U")
    imprime(matriz)
    return matriz_p, matriz_l, matriz

def trocarOrdem(matriz,vet):
    vet_resp = []
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == 1:
                vet_resp.append(vet[j])
    return vet_resp

def resolverSistema(matriz,vet_b):
    matriz_p, matriz_l, matriz_u = decompor(matriz)
    vet_b = trocarOrdem(matriz_p,vet_b)
    print(vet_b,end='\n\n')
    vet_y = triangular_superior(matriz_l,vet_b)
    print(vet_y,end='\n\n')
    vet_x = triangular_inferior(matriz_u,vet_y)
    print(vet_x, end='\n\n')

def triangular_superior(matriz,vet):
    vet_resp = []
    for i in range(len(matriz)):
        soma = 0
        for j in range(i):
            soma += matriz[i][j]*vet_resp[j]
        vet_resp.append((vet[i]-soma)//matriz[i][i])
    print(vet_resp)
    return vet_resp

def triangular_inferior(matriz,vet):
    vet_resp = [0 for x in range(len(matriz))]
    for i in range(len(matriz)-1,-1,-1):
        soma = 0
        for j in range(len(matriz)-1,i-1,-1):
            soma += matriz[i][j]*vet_resp[j]
        vet_resp[i] = (vet[i]-soma)//matriz[i][i]
    print(vet_resp)
    return vet_resp

if __name__ == '__main__':
    matriz =    [[2,-1,4,0],
                [4,-1,5,1],
                [-2,2,-2,3],
                [0,3,-9,4]]
    # decompor(matriz)
    # matriz =    [[1,0,0],
    #             [2,1,0],
    #             [-1,0,1]]
    # b = [2,-1,1]
    # resolverSistema()
    # triangular_superior(matriz,b)
    # matriz =    [[2,3,-1],
    #             [0,-2,1],
    #             [0,0,3]]
    # b = [4,-7,13,-13]
    # matriz =    [[2,2,1,1],
    #             [0,-1,-1,-5],
    #             [0,0,3,13],
    #             [0,0,0,-13]]
    # triangular_inferior(matriz,b)
    # triangular_inferior(matriz,b)
    # matriz =    [[2,3,-1],
    #             [4,4,-1],
    #             [-2,-3,4]]
    # decompor(matriz)
    b = [5,9,1,-2]
    resolverSistema(matriz,b)
