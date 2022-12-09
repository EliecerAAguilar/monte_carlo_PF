from tabulate import tabulate
import math
import random
from typing import List

class Ejemplo07:
    """CLase del Ejemplo #7 Estrategias de Servicio"""
    def cola(self, n: int) -> None:
        """
        metodo para generar los valores de cola
        :param n: cantidad maxima de valores a generar para la coda
        :return: Nada
        :rtype None
        """
        data: List[tuple] = []
        serviceTimeTotal = 0
        for i in range(n):
            nTiempoArribo=int(random.uniform(0,100))
            tiempoLlegadas=0

            if 14>= nTiempoArribo >=0:
                tiempoLlegadas=0.5

            if 39>= nTiempoArribo >=15:
                tiempoLlegadas=1.0

            if 40>= nTiempoArribo >=69:
                tiempoLlegadas=1.5

            if 70 >= nTiempoArribo >=94:
                tiempoLlegadas=2.0

            if 95 >= nTiempoArribo >=99:
                tiempoLlegadas=2.5


            r=int(random.uniform(1,10))
            tiempoServicio=1.2*math.log(r)

            serviceTimeTotal+=tiempoServicio

            data.append((i+1,nTiempoArribo,tiempoLlegadas,r,tiempoServicio))




        self.present(data)

        tiempoTotalServicio=serviceTimeTotal+0.3+0.2

        CT=5*(tiempoTotalServicio)+20*(8*8)
        print('Costo del Sistema (CT): {}'.format(CT))

        print('Costo promedio por hora (CT): {}'.format(CT/8.8))


    def present(self, data: List[tuple]) -> None:
        """
        Metodo para presentar/ Imprimir los valores de la simulacion
        :param data: datos de la simulacion
        :type data: List[tuple]
        :return: Nada
        :rtype None
        """
        headers = [ '# de llegadas',
                    'Tiempo entre Arribo',
                    'Tiempo entre llegadas',
                    'Tiempo de Servicio # random',
                    'Tiempo de Servicio',
                    ]

        print(tabulate(data, headers=headers, showindex=False))

    def run(self):
        """
        Metodo para ejecutar la simulacion del ejemplo #7
        :return: Nada
        :rtype None
        """
        print('ESTRATEGIAS DE SERVICIOS (Colas)')
        n: int = int(input('Introduzca número de llegadas: '))
        self.cola(n)

