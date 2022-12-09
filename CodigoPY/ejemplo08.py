import math
import random
import matplotlib.pyplot as plt
from typing import List


class Ejemplo08:
    """Clase para el desarrollo del ejemplo #8"""
    def genUnif(self, ctd: int) -> List[float]:
        """
        Metodo para generar los valores pseudo aleatorios uniformes
        :param ctd: cantida de valores a generar
        :type ctd: int
        :return: lista con los valores aleatorios
        :rtype List[float]
        """
        lista: List[float] = []
        for i in range(ctd):
            lista.append(random.uniform(0,1))
        return lista


    def genExpo(self, r: List[float], lmb: float) -> List[float]:
        """
        Meotodo para generar los valores exponenciales a partir del valor de r
        :param r: lista de valores aleatorios uniformes
        :type r: List[float]
        :param lmb: valor de la media
        :type lmb: float
        :return: lista con los valores generados
        :rtype List[float]
        """
        lista: List[float] = []
        for elem in r:
            x = -(1/lmb)*(math.log(elem))
            lista.append(x)
        return lista


    def run(self):
        ctdNums: int = int(input("Cuantos numeros desea generar: "))

        r: List[float] = self.genUnif(ctdNums)

        lmb:float = 0.5
        x: List[float] = self.genExpo(r, lmb)

        plt.figure()
        plt.title('Distribucion de numeros aleatorios uniformes')
        plt.hist(r)
        plt.show()

        plt.figure()
        plt.title('Distribucion de numeros aleatorios exponenciales (Por Transformada Inversa)')
        plt.hist(x, bins=20)
        plt.show()

