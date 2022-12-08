from tabulate import tabulate
import math
import random
from typing import List

class Ejemplo05:
    """Clase para el desarrollo del Ejemplo #5"""
    def calculoPi(self,long: int,n: int) -> None:
        """
        Metodo para realizar los calculos de la simulacion
        :param long: longitud de las agujas en cm
        :type long: int
        :param n: cantidad de lanzamientos a realizar
        :type n: int
        :return: Nada
        :rtype: None
        """
        data: List[tuple] = []
        aciertos: int = 0
        for i in range(n):
            r1: float = random.uniform(0,1)
            x: float = r1*(long/2.0)
            r2: float = random.uniform(0,1)
            y: float = (long/2.0)*math.sin(180*r2)

            if x<=y:
                aciertos+=1
                textAcierto = '\u2713'
            else:
                textAcierto = '\u274C'

            data.append((r1,x,r2,y,textAcierto))

        self.present(data)

        vpi: float = n/aciertos

        print(f'N: {n}')
        print(f'Aciertos: {aciertos}')
        print(f'Valor aproximado de PI: {vpi}')

    def present(self,data: List[tuple]) ->None:
        """
        Imprime los valores de la simulacion en formato de tabla
        :param data: lista con los valores a mostrar
        :type data: List[tuple]
        :return: Nada
        :rtype None
        """
        headers = [ 'r1',
                    'x',
                    'r2',
                    'Pi*r2',
                    'Y',
                    'Acierto'
                    ]

        print(tabulate(data, headers=headers, showindex=True))

    def run(self)-> None:
        """
        Metodo para ejecutar el Ejemplo #5
        Pide los datos para ejecutar la simulacion por medio de la aguja de buffon
        :return:
        :rtype None
        """
        print('CALCULO DEL VALOR DE PI')
        long = int(input('Introduzca longitud de la aguja(cms): '))
        n = int(input('Introduzca cantidad de lanzamientos: '))
        print('-------------------------')
        print('CALCULO DEL VALOR DE PI')
        print('Longitud de la Aguja (cms) ==> ',long)
        print('Número de lanzamientos (cms) ==> ',n)
        self.calculoPi(long,n)

