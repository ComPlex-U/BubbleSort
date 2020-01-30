from time import clock
from random import randrange

def bubbleSort(A):
    for i in range(0, len(A)):
        for j in range(len(A)-1,i,-1):
            if A[j] < A [j-1]:
                A[j], A[j-1] = A[j-1], A[j]

def teste(tamanho):
    n= []
    # Gerar numeros aleatorios e adiciona-lo á lista
    for i in range(tamanho):
        num = randrange(1000)
        n.append(num)
    print("array nao-organizzada :: ",n)

    tR = clock()
    bubbleSort(n)
    tF = clock()

    print("array organizada :: ",n )
    print("tempo de organização :: {} ms".format( (tF - tR) * 1000) )

teste(10)