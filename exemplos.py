def main ():
    matriz = []
    nlinhas = int(input("Digite um numero de linhas na matriz: "))
    ncolunas = int(input("Digite um numero de colunas na matriz: "))

    carrega_matriz(matriz, nlinhas, ncolunas)
    exibe_matriz(matriz, nlinhas)
    print(f"Somatorio dos elementos da matriz: {calcula_somamatriz(matriz, nlinhas, ncolunas)}")
    exibe_paresmatriz(matriz, nlinhas, ncolunas)



def carrega_matriz(matriz,nlin,ncol):
    for lin in range(0,nlin):
        linha = []
        for col in range(0,ncol):
            linha.append(int(input("Digite um elemento da matriz: ")))
        matriz.append(linha)

def calcula_somamatriz(matriz,nlin,ncol):
    soma = 0
    for lin in range(0,nlin):
        for col in range(0,ncol):
            soma+=matriz[lin][col]

    return(soma)

def exibe_paresmatriz(matriz,nlin,ncol):
    for lin in range(0,nlin):
        for col in range(0,ncol):
            if (matriz[lin][col] % 2 == 0):
                print(matriz[lin][col])

def exibe_matriz(matriz,nlin):
    for lin in range(0,nlin):
        print(matriz[lin])

if (__name__ == "__main__"):
    main()