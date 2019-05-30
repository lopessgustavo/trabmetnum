
#mover o maior pivo para cima
def moverPivo(matriz,linha,coluna):
    maior = linha
    for i in range(linha,len(matriz)):
        if abs(matriz[i][coluna]) > abs(matriz[maior][coluna]):
            maior = i
    matriz[linha], matriz[maior] = matriz[maior], matriz[linha]

def imprime(matriz):
    for linha in matriz:
        print(linha)
    print("\n")


def matrizZeros(tam):
    matriz = []
    for i in range(0,tam):
        linha = [0 for j in range(tam)]
        matriz.append(linha)
    return matriz


def a(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if(matriz[i][i]) == 0:
                matriz[i] = matriz[i] + matriz[j]
                break
    
    pass

#subtrair l2 em l1
def subtrairLinhas(l1,l2,multiplicador):
    for i in range(len(l1)):
        l1[i] = l1[i] - l2[i]*multiplicador



def zerarColuna(matriz,coluna):
    for i in range(coluna+1,len(matriz)):
        multiplicador = matriz[i][coluna]/matriz[coluna][coluna]
        subtrairLinhas(matriz[i],matriz[coluna],multiplicador)
        



def fatLU(matriz):
    # a(matriz)
    matriz_l = matrizZeros(len(matriz))
    for i in range(len(matriz)-1):
        moverPivo(matriz,i,i)
        zerarColuna(matriz,i)
        # imprime(matriz)
        # for j in range(i):
        # for k in range(i,len(matriz)):
            # matriz_l[k][i] = matriz[k][i]/matriz[i][i]
    imprime(matriz)





linhas = int(input())
colunas = int(input())
matriz = []
for i in range(linhas):
    linha = input().split(" ")
    linha = [int(x) for x in linha]

    matriz.append(linha)
fatLU(matriz)

# imprime(matrizZeros(linhas))
# moverPivo(matriz,0,0)
# imprime(matriz)
