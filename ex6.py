#Exercício 6

def main():
    lista_numero = []
    tam = int(input("Digite o tamanho da lista: "))
    carrega_lista(lista_numero, tam)
    soma,media = calcula_somaedia(lista_numero,tam)
    print(f"Somatorio dos elementos da lista: {soma}")
    print(f"Media dos elementos da lista: {media}")


def carrega_lista(lista_numeros, tam):
    for i in range(0, tam):
        lista_numeros.append(int(input("Digite um elemento da lista: ")))


def calcula_somaedia(lista_numeros,tam):
    soma = 0
    for  i in range(0,tam):
        soma+=lista_numeros[i]

    media = soma / tam
    return(soma,media)

if (__name__ == "__main__"):
    main()