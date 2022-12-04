from tabulate import tabulate
import math
import random

def present(data):
    headers = [ 'r1',
                'x', 
                'f(x)',
                'r2',
                'Y', 
                'Aciertos',
                'Área'
                ]

    print(tabulate(data, headers=headers, showindex=True))


def areaBajoCurva(a,b,fmax,n):
    data=[]
    #Pasos: Queremos imprimir el area cada n para ir comparando, asi que pasos defi cada cuantas iteraciones se imprime el area.
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
            area = (aciertos/(i+1))*(b-a)
        else:
            area = ''
        
        data.append((
            r1, xi, fxi, r2, yi,  textAciertos, area
        ))

    present(data)
    area = (aciertos/(n))*(b-a)    

    print('Valor aproximado del Area: {}'.format(area))
    




def run():
    #Lectura de datos
    print('CALCULO DEL AREA BAJO LA CURVA para la funcion f(x) = sin(pi*x)/(pi*x)')
    a = int(input('Introduzca el limite inferior (a): '))
    b = int(input('Introduzca el limite superior (b): '))
    fmax = int(input('Introduzca el valor máximo de la función (Fmax): '))
    n = int(input('Introduzca el número de puntos a simular (n): '))
    n = n+1

    areaBajoCurva(a,b,fmax,n)

run()