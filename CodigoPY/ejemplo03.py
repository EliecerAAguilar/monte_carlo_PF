import matplotlib.pyplot as plt
from numpy import random
from typing import List

class Ejemplo03:
    """
    clase para el desarollo del ejemplo #03
    """
    def setVar(self, vals: List[int | float], inters: List[int | float], n: int) -> List[int | float]:
        """
        Metodo para definir los valores de y
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
        :param vals: tomaria los valores 0 a 3 'y'
        :type vals: List[int | float]
        :param inters: tomaria los valores 15, 40, 83 y 99
        :type inters: List[int | float]
        :param n: Numero de valores de la lista
        :type n: int
        :return lista con los valores
        :rtype List[int|float]
        """
        lista: List[int | float] = []
        interIndex: int = 0
        for i in range(n+1):
            if i<= inters[interIndex]:
                pass
            else:
                interIndex +=1
            lista.append(vals[interIndex])
        return lista

    def getVar(self, num: int, y: List[int | float]) -> int | float:
        """
        Obtener el valor e Y
        :param num: indice a buscar
        :type num: int
        :param y: lista con los valores
        :type y: List[int | float]
        :return: el valor deseado
        :rtype int | float
        """
        return y[num]


    def present(self, w: List[int | float]) -> None:
        """
        Imprime los valores en pantalla en un grafico
        :param w: lista con los valores a graficar
        :return: nada
        :rtype None
        """
        plt.hist(w, bins=[5,10,15,20,25,32])
        plt.title("Histograma de Distribución de W")
        plt.show()


    def randoms(self, n: int,maxi:int) -> List[int]:
        """
        metodo para generar los valores pseudo aleatorios enteros
        :param n: tamano de la lista a generar
        :type n: int
        :param maxi: valor maximo de los valores pseudo aleatorios
        :type maxi: int
        :return: lista de numeros pseudo aleatorios
        :rtype List[int]
        """
        lista: List[int] = []
        for i in range(n):
            lista.append(random.randint(0,maxi))
        return lista

    def funcEfectividad(self, x: List[int] ,y: List[int] ,z: List[int] ,n: int) -> None:
        """
        metodo para medir la efectividad
        :param x: Lista con los valores de X
        :type x:
        :param y: Lista con los valores de Y
        :type y: List[int]
        :param z: Lista con los valores de Z
        :type z: List[int]
        :param n: cantidad de veces a ejecutar este analisis
        :type n: int
        :return: Nada
        :rtype None
        """
        #Utilizaremos los nuemeros aleatorios del ejemplo:
        randX: List[int]  = self.randoms(n, maxi=99)
        randY: List[int]  = self.randoms(n,maxi=99)
        randZ: List[int]  = self.randoms(n,maxi=9)

        #Inicializamos la data:
        w: List[int] = []
        for i in range(n):
            xi: int = self.getVar(randX[i], x)
            yi: int = self.getVar(randY[i], y)
            zi: int = self.getVar(randZ[i], z)

            wi: int = xi+4*yi+3*zi

            w.append(wi)

        self.present(w)


    def run(self) -> None:
        """
        Metodo para ejecutar el ejemplo #3
        Definicion de variables para la ecuacion W = X + 4Y + 3Z
        X definida en base al enunciado
        :return: nada
        :rtype None
        """

        x = self.setVar(
            vals=[x+1 for x in range(6)],
            inters=[9, 29, 54, 79, 94, 99],
            n = 99
        )

        y = self.setVar(
            vals=[x+1 for x in range(4)],
            inters=[24, 54, 79, 99],
            n = 99
        )

        z = self.setVar(
            vals=[x+1 for x in range(3)],
            inters=[2,7,9],
            n = 9
        )

        n= int(input('¿Cuantas veces desea correr la simulacion de w?: '))
        self.funcEfectividad(x,y,z,n)
