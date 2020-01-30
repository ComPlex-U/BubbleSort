from time import clock
from random import randrange
import statistics

def bubbleSort(A):
    for i in range(0, len(A)):
        for j in range(len(A)-1,i,-1):
            if A[j] < A [j-1]:
                A[j], A[j-1] = A[j-1], A[j]

def teste(numeroListas, tamanho):
    tempos = []
    # Gerar numeros aleatorios e adiciona-lo á lista
    for k in range(numeroListas):
        n = []
    for i in range(tamanho):
        num = randrange(1000)
        n.append(num)

    print("array nao-organizzada :: ". format(k+1,n))

    tI = clock()
    bubbleSort(n)
    tF = clock()
    tempos.append(tF - tI)

    print("array organizada :: ".format(k+1, n))
    print("tempo de organização :: {} ms".format( (tF - tI)) )
print("Media Pytho :: {}s".format(statistics.mean(tempos)))


numeroListas = 10
tamanhoLista = 100
teste(numeroListas, tamanhoLista)