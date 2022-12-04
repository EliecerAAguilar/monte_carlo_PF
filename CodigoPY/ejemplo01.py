import matplotlib.pyplot as plt
from tabulate import tabulate
from numpy import random
from typing import List


class Ejemplo01:
    """""
    Clase Ejemplo 01 de simulacion monte carlo desde los programas en java a Python
    desarrollo del primer enunciado
    utilizando Programacion orientada a objetos
    """
    def plot_title(self, x: List[int | float], y: List[int | float], color: str, xlabel: str, ylabel: str, title: str) -> None:
        """
        graficar los valores
        :param x: lista de valores enteros o flotantes para el eje de las X
        :type x: List[int | float]
        :param y: lista de valores enteros o flotantes para el eje de las Y
        :type y: List[int | float]
        :param color: color de las lineas
        :type color: str
        :param xlabel: etiqueta del eje X
        :type xlabel: str
        :param ylabel: etiqueta del eje Y
        :type ylabel: str
        :param title: titulo del grafico
        :type title: str`
        :return: nada
        :rtype: None
        """
        plt.figure()
        plt.plot(x, y, color)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()

    def calcular_val_rand(self, x: int, y: List[int | float]) -> float | int:
        """
        Calcular y de una lista de elementos
        :param x:
        :type x: int
        :param y:
        """
        return y[x]

    def tiempo_descompostura_y(self, nums: List[int | float]) -> List[int | float]:
        """
        Calculo de 'Y' de descompostura
        Funcion que asigna la Y de los tiempos de descompostura
        :param nums
        :type nums: List[int | float]
        :returns: una lista de enteros o flotantes
        :rtype: List
        """
        lista = []
        for i in range(1, 101):
            if i <= 5:
                lista.append(nums[0])
            elif i <= 19:
                lista.append(nums[1])
            elif i <= 38:
                lista.append(nums[2])
            elif i <= 60:
                lista.append(nums[3])
            elif i <= 77:
                lista.append(nums[4])
            elif i <= 85:
                lista.append(nums[5])
            elif i <= 90:
                lista.append(nums[6])
            elif i <= 95:
                lista.append(nums[7])
            elif i <= 99:
                lista.append(nums[8])
            elif i == 100:
                lista.append(nums[9])
        return lista

    def tiempo_reparacion_y(self, nums: List[int | float]) -> List[int | float]:
        """
        Funciones de calculo de 'Y' de reparacion
        Funcion que asigna la 'Y' de los tiempos de descompostura
        :param nums: lista
        :type nums:  List[int | float]
        :return: una lista de enteros o flotantes
        :rtype: List[int | float]
        """
        lista = list()
        for i in range(1, 101):
            if i <= 3:
                lista.append(nums[0])
            elif i <= 7:
                lista.append(nums[1])
            elif i <= 18:
                lista.append(nums[2])
            elif i <= 40:
                lista.append(nums[3])
            elif i <= 59:
                lista.append(nums[4])
            elif i <= 75:
                lista.append(nums[5])
            elif i <= 86:
                lista.append(nums[6])
            elif i <= 93:
                lista.append(nums[7])
            elif i <= 97:
                lista.append(nums[8])
            elif i <= 99:
                lista.append(nums[9])
            else:
                lista.append(nums[10])
        return lista

    # --------------
    def tdescompuesto(self, x) -> List:
        """
        CALCULO DE TIEMPO DESCOMPUESTO
        :param x:
        :return: una lista
        :rtype: List
        """
        y = self.tiempo_descompostura_y([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

        # Grafica de probabilidad acumulada
        # plot_title(x,y, color='g', xlabel1='Valores', ylabel1='Probabilidades', title1='Probabilidad de Tiempo de descompostura')
        # Prueba de tiempos de descompostura
        # calcularValRand([83,97,88,12,22,16,24,64,37,62], y)
        return y

    def tiempo_reparacion(self, x) -> List:
        """
        CALCULO DE TIEMPO DE REPARACION
        :param x:
        :type x: List
        :return: una lista
        :rtype: List
        """
        y = self.tiempo_reparacion_y([8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
        # Grafica de probabilidad acumulada
        # plot_title(x,y, color='g', xlabel1='Valores', ylabel1='Probabilidades', title1='Probabilidad de Tiempo de descompostura')
        # Prueba de tiempos de descompostura
        # calcularValRand([91,4,72,12,30,32,91,29,33,8], y)
        return y

    def present(self, data) -> None:
        """
        Impresion de resultados
        :param data:
        :type: data: List[int | float]
        :return: nada
        :rtype: None
        """
        headers = ['Tiempo Descompostura',
                   'Inicio tiempo de reparación',
                   'Fin tiempo de reparación',
                   'Tiempo de espera de la máquina',
                   'Tiempo ocioso del mecánico de reparación'
                   ]

        print(tabulate(data, headers=headers))

    def randoms(self, n: int) -> List[int]:
        """
        metodo para generar los valores pseudo aleatorios
        :param n: cantidad maxima de valores a generar
        :type n: int
        :return: Lista de entereros
        :rtype: List[int]
        """
        lista = []
        for i in range(n):
            lista.append(random.randint(1, 100))
        return lista

    def simulacion(self, x, yDesc, yRepar):
        # Numeros Aleatorios
        randomDes = self.randoms(30)
        randomRepar = self.randoms(30)

        # inicializacion de variables
        data = []
        tDescompostura = 0
        tInicioReparacion = 0
        tEsperaMaquina = 0
        tMecanicoOcioso = 0
        # Primera corrida
        tFinReparacion = tInicioReparacion + self.calcular_val_rand(randomRepar[0], yRepar)
        data.append(
            (
                tDescompostura,
                tInicioReparacion,
                tFinReparacion,
                tEsperaMaquina,
                tMecanicoOcioso
            )
        )
        for i in range(1, 30):
            # Calculo del tiempo de descompostura
            tDescompostura = tDescompostura + self.calcular_val_rand((randomDes[i] - 1), yDesc)

            # Funcion Lambda para calculo de fin de reparacion
            inicioReparacion = lambda tdesc, tfin: tdesc if tfin < tdesc else tfin

            # Calculo inicio Reparacion
            tInicioReparacion = inicioReparacion(tDescompostura, tFinReparacion)

            # Guardamos el fin de la corrida anterior
            tFinReparacionAnterior = tFinReparacion

            # Calculo de fin de reparacion
            tFinReparacion = tInicioReparacion + self.calcular_val_rand(randomRepar[i] - 1, yRepar)

            # Caluclo de tiempo de espera de maquina
            tEsperaMaquina = tInicioReparacion - tDescompostura

            # Calculo del tiempo ociosos del mecanico
            tMecanicoOcioso = tInicioReparacion - tFinReparacionAnterior

            # Guardar datos para presentacion de tabla
            data.append((tDescompostura, tInicioReparacion, tFinReparacion, tEsperaMaquina, tMecanicoOcioso))

        self.present(data)

    def run(self):
        """
        metodo para ejecutar el ejemplo #1
        :return: nada
        :rtype: None
        """
        # Definicion de los datasets para la simulacion
        x = [x for x in range(1, 101)]  # Creacion de los valores de x
        yDesc = self.tdescompuesto(x)
        yRepar = self.tiempo_reparacion(x)

        # Inicio de simulacion
        self.simulacion(x, yDesc, yRepar)
