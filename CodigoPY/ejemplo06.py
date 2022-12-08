from tabulate import tabulate
from typing import List
import random


class Ejemplo06:
    """clase para el desarrollo del Ejemplo #6 Tambaleo del borracho
    """
    def borracho(self, n: int) -> None:
        """
        metodo para ejecutar los calculos necesarios en la simulacion del tambaleo del borracho
        :param n: cantidad de veces a ejecutar los calculos
        :type n: int
        :return: Nada
        :rtype None
        """
        data: List[tuple] = []
        x: int =0
        y: int =0
        for i in range(n):
            r: float = random.uniform(0,100)


            if 0 <= r < 25:
                y+=1

            if 25 <= r < 50:
                y-=1

            if 50 <= r < 75:
                x+=1
            if 75 <= r <100:
                x-=1

            data.append((i,r,x,y))

        self.present(data)

        if abs(x) + abs(y) >= 2:
            print("El borracho termino a 2 o mas cuadras de donde estaba inicialmente.")
        else:
            print("El borracho termino a menos de 2 cuadras de donde estaba inicialmente.")


    def present(self, data: List[tuple]) -> None:
        """
        Metodo para presentar/ imprimir los valores de la simulacion por consola
        :param data: informacion recopilda de la simulacion para imprimir
        :type data: List[tuple]
        :return: Nada
        :rtype None
        """
        headers = [ '# Cuadras',
                    '# Aleatorio',
                    'Loc. X',
                    'Loc. Y',
                    ]

        print(tabulate(data, headers=headers, showindex=False))



    def run(self) -> None:
        """Metodo para ejecucar la simulacion del tambaleo del borracho y pedir la informacion necesaria
        para la cantidad de veces a correr el algoritmo
        :return nada
        :rtype None
        """
        print('SIMULACION DEL TAMBALEO DEL BORRACHO')
        n: int = int(input('Cual es el valor de n: '))
        print('-------------------------')
        self.borracho(n)

