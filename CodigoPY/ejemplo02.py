from tabulate import tabulate
from numpy import random
from typing import List


class Ejemplo02:
    """
    clase Ejemplo #2
    """
    def setY(self, vals: List[int | float], inters: List[int | float]) -> List[int | float]:
        """
        Metodo para definir los valores de y
        :param vals:
        :type:vals: List[int | float]
        :param inters:
        :type:inters: List[int | float]
        :return: lista de valores
        :rtype: List[int | float]
        """
        lista = list()
        interIndex = 0
        for i in range(100):
            if i<= inters[interIndex]:
                pass
            else:
                interIndex +=1
            lista.append(vals[interIndex])
        return lista

    def getY(self, num: int, y: List[int | float]) -> int | float:
        """

        :param num: indice
        :type:num:int
        :param y: lista a buscar
        :type y: List
        :return: valor entero
        :rtype: int | float
        """
        return y[num]

    def present(self, data: List[tuple]) -> None:
        """
        impresion de los resultados
        :param data: informacion a imprimir
        :type: data: List[tuple]
        :return: nada
        :rtype: None
        """
        headers = ['Día', 'Demanda']
        print(tabulate(data, headers=headers))

    def randoms(self, n: int) -> List:
        """
        metodo para generar los valores pseudo aleatorios
        hasta un rango especificado
        :param n: valor maximo de valores a generar
        :type: n: int
        :returns: una lista de valores pseudo aleatorios
        :rtype: List
        """
        lista = []
        for i in range(n):
            lista.append(random.randint(0, 99))
        return lista

    def montecarlo(self, x: List[int | float], y: List[int | float]) -> None:
        """
        simulacion de montecarlo
        :param x:
        :type x: List[int | float]
        :param y:
        :type y: List[int | float]
        :return: nada
        :rtype: None
        """

        randNums = self.randoms(10)
        data = []

        for i in range(1, 11):
            demanda = self.getY(randNums[i-1], y)
            data.append((i, demanda))

        self.present(data)

    def run(self) -> None:
        """Definimos los valores de x que es de 0 a 99
            de 'Y' dados por la distribucion mostrada en la funcion
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
        :returns: nada
        :rtype: None
        """
        x = [x for x in range(100)]
        vals = [x for x in range(6)]
        inters = [4, 14, 29, 59, 84, 99]
        y = self.setY(vals, inters)

        self.montecarlo(x, y)
