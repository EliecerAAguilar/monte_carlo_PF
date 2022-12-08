import numpy as np
from tabulate import tabulate
import math
import random
from typing import List

class Ejemplo04:
    def present(self, data: List[tuple]) -> None:
        """
        meotodo para imprimir los valores
        :param data:
        :type data: List[tuple]
        :return: Nada
        :rtype None
        """
        headers = [ 'r1',
                    'x',
                    'f(x)',
                    'r2',
                    'Y',
                    'Aciertos',
                    'Área'
                    ]

        print(tabulate(data, headers=headers, showindex=True))

    def areaBajoCurva(self, a: int,b: int,fmax: int,n: int) -> None:
        """Pasos: Queremos imprimir el area cada n para ir comparando,
         asi que pasos defi cada cuantas iteraciones se imprime el area
        :param a: limite inferior
        :type a: int
        :param b: limite superior
        :type b: int
        :param fmax: valor maximo de la funcion
        :type fmax: int
        :param n: numero de puntos a simular
        :type n: int
        :return Nada
        :rtype None
        """
        data=[]
        pasos = 5
        aciertos = 0
        for i in range(n):

            r1 = random.uniform(0,1)
            xi = r1*(b-a)+a
            fxi = math.sin(math.pi*xi)/(math.pi*xi)
            r2 = random.uniform(0,1)
            yi = r2*fmax

            if yi <= fxi:
                aciertos += 1
                textAciertos = '\u2713'
            else:
                textAciertos = '\u274C'

            if i % pasos == 0:
                area:float = (aciertos/(i+1))*(b-a)
            else:
                area = np.NAN

            data.append((r1, xi, fxi, r2, yi,  textAciertos, area))

        self.present(data)
        area = (aciertos/ n)*(b-a)

        print(f"Valor aproximado del Area: {area}")


    def run(self) -> None:
        """
        metodo para ejecutar el Ejemplo #4 Area bajo la curva
        :return: Nada
        :rtype None
        """
        print("CALCULO DEL AREA BAJO LA CURVA para la funcion f(x) = sin(pi*x)/(pi*x)")
        a: int = int(input("Introduzca el limite inferior (a): "))
        b: int = int(input("Introduzca el limite superior (b): "))
        fmax: int = int(input("Introduzca el valor máximo de la función (Fmax): "))
        n: int = int(input("Introduzca el número de puntos a simular (n): "))
        n = n+1

        self.areaBajoCurva(a,b,fmax,n)
