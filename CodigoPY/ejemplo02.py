import matplotlib.pyplot as plt
from tabulate import tabulate
from numpy import random

#Funcion para definir los valores de y 
def setY(vals, inters):
    lista = list()
    interIndex = 0
    for i in range(100):
        if i<= inters[interIndex]:
            pass
        else: 
            interIndex +=1
        lista.append(vals[interIndex])
    return lista

def getY(num, y):
    return y[num]

def present(data):
    headers = ['Día','Demanda']
    print(tabulate(data, headers=headers))

def randoms(n):
    lista = []
    for i in range(n):
        lista.append(random.randint(0,99))
    return lista

def montecarlo(x,y):
    randNums = randoms(10)
    data = []
    for i in range(1,11):
        demanda = getY(randNums[i-1], y)
        data.append((i, demanda))
    present(data)

def run():
    #Definimos los valores de x que es de 0 a 99
    x = [x for x in range(100)]
    '''Definimos los valores de y dados por la distribucion mostrada en la funcion
            Para esto creamos dos listas: 
                1. vals: valores que tomara y en cada intervalo
                2. inters: Valor superior del intervalo de numeros que toman los valores
            Importante que vals y clases tengan la misma cantidad de elementos.
            Ejemplo: 
                valores     |     intervalo
                   0        |        0-15         
                   1        |       16-40
                   2        |       40-83
                   3        |       83-99
            vals tomaria los valores 0 a 3 y
            inters tomaria los valores 15, 40, 83 y 99
    '''
    vals = [x for x in range(6)]
    inters = [4,14,29,59,84,99]
    y = setY(vals, inters)

    montecarlo(x,y)

run()
