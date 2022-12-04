import matplotlib.pyplot as plt
from numpy import random

#Funcion para definir los valores de y 
def setVar(vals, inters, n):
    '''
    DESCRIPCION DE LA FUNCION SETVAR
    Definimos los valores de y dados por la distribucion mostrada en la funcion
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
            n: Numero de valores de la lista
    '''
    lista = list()
    interIndex = 0
    for i in range(n+1):
        if i<= inters[interIndex]:
            pass
        else: 
            interIndex +=1
        lista.append(vals[interIndex])
    return lista

def getVar(num, y):
    return y[num]



def present(W):
    plt.hist(W, bins=[5,10,15,20,25,32]) 
    plt.title("Histograma de Distribución de W") 
    plt.show()
    

def randoms(n,maxi):
    lista = []
    for i in range(n):
        lista.append(random.randint(0,maxi))
    return lista

def funcEfectividad(x,y,z,n):
    #Utilizaremos los nuemeros aleatorios del ejemplo: 
    randX = randoms(n, maxi=99)
    randY = randoms(n,maxi=99)
    randZ = randoms(n,maxi=9)

    #Inicializamos la data:
    w = []
    for i in range(n):
        xi = getVar(randX[i], x)
        yi = getVar(randY[i], y)
        zi = getVar(randZ[i], z)

        wi = xi+4*yi+3*zi

        w.append(wi)
    present(w)


def run():
    #Definicion de variables para la ecuacion W = X + 4Y + 3Z
    #_X definida en base al enunciado
    x = setVar(
        vals=[x+1 for x in range(6)],
        inters=[9, 29, 54, 79, 94, 99],
        n = 99
    )
    #_Y
    y = setVar(
        vals=[x+1 for x in range(4)],
        inters=[24, 54, 79, 99],
        n = 99
    )
    #_Z 
    z = setVar(
        vals=[x+1 for x in range(3)],
        inters=[2,7,9],
        n = 9
    )

    n= int(input('¿Cuantas veces desea correr la simulacion de w?: '))
    funcEfectividad(x,y,z, n)

run()