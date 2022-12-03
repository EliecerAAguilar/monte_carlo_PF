import matplotlib.pyplot as plt
from tabulate import tabulate
from numpy import random
from typing import List, Set


def plottit(x:float, y, color, xlabel, ylabel, title) -> None:
    """
    graficar los valores
    :param x:
    :param y:
    :param color:
    :param xlabel:
    :param ylabel:
    :param title:
    :return: None
    """
    plt.figure()
    plt.plot(x, y, color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()


def calcular_val_rand(x: int, y: List) -> float:
    """
    Calcular y de una lista de elementos
    :param x: <int>
    :param y: <List>
    """
    return y[x]


def tiempo_descompostura_y(nums) -> List:
    """
    Calculo de y de descompostura
    Funcion que asigna la Y de los tiempos de descompostura
    :param nums: int
    :return: List
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


# -----------------------Funciones de: Calculo de y de reparacion-----------------
# Funcion que asigna la Y de los tiempos de descompostura
def trep(nums) -> List:
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


# --------CALCULO DE TIEMPO DESCOMPUESTO------
def tdescompuesto(x) -> List:
    y = tiempo_descompostura_y([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])  # Distribucion de y

    # Grafica de probabilidad acumulada
    # plottit(x,y, color='g', xlabel1='Valores', ylabel1='Probabilidades', title1='Probabilidad de Tiempo de descompostura')
    # Prueba de tiempos de descompostura
    # calcularValRand([83,97,88,12,22,16,24,64,37,62], y)
    return y


# ----------CALCULO DE TIEMPO DE REPARACION--------
def tReparacion(x) -> List:
    y = trep([8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    # Grafica de probabilidad acumulada
    # plottit(x,y, color='g', xlabel1='Valores', ylabel1='Probabilidades', title1='Probabilidad de Tiempo de descompostura')
    # Prueba de tiempos de descompostura
    # calcularValRand([91,4,72,12,30,32,91,29,33,8], y)
    return y


# Impresion de resultados
def present(data) -> None:
    headers = ['Tiempo Descompostura',
               'Inicio tiempo de reparación',
               'Fin tiempo de reparación',
               'Tiempo de espera de la máquina',
               'Tiempo ocioso del mecánico de reparación'
               ]

    print(tabulate(data, headers=headers))


# -----------------SIMULACION-----------
# def present(data) -> None:
#     headers = ['t Descomp',
#                'Inicio t reparar',
#                'Fin t reparar',
#                't de espera',
#                'tiempo mecanico ocioso'
#                ]
#
#     print(tabulate(data, headers=headers, showindex=True))


def randoms(n: int) -> List:
    lista = []
    for i in range(n):
        lista.append(random.randint(1, 100))
    return lista


def simulacion(x, yDesc, yRepar):
    # Numeros Aleatorios
    randomDes = randoms(30)
    randomRepar = randoms(30)

    # inicializacion de variables
    data = []
    tDescompostura = 0
    tInicioReparacion = 0
    tEsperaMaquina = 0
    tMecanicoOcioso = 0
    # Primera corrida
    tFinReparacion = tInicioReparacion + calcular_val_rand(randomRepar[0], yRepar)
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
        tDescompostura = tDescompostura + calcular_val_rand((randomDes[i] - 1), yDesc)  # Calculo del tiempo de descompostura

        inicioReparacion = lambda tdesc, tfin: tdesc if tfin < tdesc else tfin  # Funcion Lambda para calculo de fin de reparacion
        tInicioReparacion = inicioReparacion(tDescompostura, tFinReparacion)  # Calculo inicio Reparacion

        tFinReparacionAnterior = tFinReparacion  # Guardamos el fin de la corrida anterior
        tFinReparacion = tInicioReparacion + calcular_val_rand(randomRepar[i] - 1, yRepar)  # Calculo de fin de reparacion

        tEsperaMaquina = tInicioReparacion - tDescompostura  # Caluclo de tiempo de espera de maquina
        tMecanicoOcioso = tInicioReparacion - tFinReparacionAnterior  # Calculo del tiempo ociosos del mecanico

        # Guardar datos para presentacion de tabla
        data.append((tDescompostura, tInicioReparacion, tFinReparacion, tEsperaMaquina, tMecanicoOcioso))

    present(data)


def run():
    # Definicion de los datasets para la simulacion
    x = [x for x in range(1, 101)]  # Creacion de los valores de x
    yDesc = tdescompuesto(x)
    yRepar = tReparacion(x)

    # Inicio de simulacion
    simulacion(x, yDesc, yRepar)

# run()
