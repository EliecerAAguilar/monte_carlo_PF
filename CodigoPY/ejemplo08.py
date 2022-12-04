import math
import random
import matplotlib.pyplot as plt

def genUnif(ctd):
    lista = []
    for i in range(ctd):
        lista.append(random.uniform(0,1))
    return lista


def genExpo(r, lmb):
    lista = []
    for elem in r:
        x = -(1/lmb)*(math.log(elem))
        lista.append(x)
    return lista


def run():
    ctdNums = int(input("Cuantos numeros desea generar: "))
    #Generacion de numeros aleatorios uniformes
    r = genUnif(ctdNums)
    #Funcion exponencial
    lmb = 0.5 #Valor de la media | Cambiable por input
    x = genExpo(r, lmb) #Generacion de numeros exponenciales a partir de r.
    
    plt.figure()
    plt.title('Distribucion de numeros aleatorios uniformes')
    plt.hist(r)
    plt.show()


    plt.figure()
    plt.title('Distribucion de numeros aleatorios exponenciales (Por Transformada Inversa)')
    plt.hist(x, bins=20)
    plt.show()
    

run()
