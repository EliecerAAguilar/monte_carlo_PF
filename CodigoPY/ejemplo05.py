from tabulate import tabulate
import math
import random

def calculoPi(long,n):
    data = []
    aciertos = 0
    for i in range(n):
        r1=random.uniform(0,1)
        x=r1*(long/2.0)
        r2=random.uniform(0,1)
        y=(long/2.0)*math.sin(180*r2)
        if(x<=y):
            aciertos+=1
            textAcierto = '\u2713'
        else:
            textAcierto = '\u274C'
        data.append((r1,x,r2,y,textAcierto))
    present(data)
    vpi=n/aciertos
    print('N: {}'.format(n))
    print('Aciertos: {}'.format(aciertos))
    print('Valor aproximado de PI: {}'.format(vpi))

def present(data):
    headers = [ 'r1',
                'x', 
                'r2',
                'Pi*r2',
                'Y', 
                'Acierto'
                ]

    print(tabulate(data, headers=headers, showindex=True))

def main():
    #Lectura de datos
    print('CALCULO DEL VALOR DE PI')
    long = int(input('Introduzca longitud de la aguja(cms): '))
    n = int(input('Introduzca cantidad de lanzamientos: '))
    print('-------------------------')
    print('CALCULO DEL VALOR DE PI')
    print('Longitud de la Aguja (cms) ==> ',long)
    print('Número de lanzamientos (cms) ==> ',n)
    calculoPi(long,n)

main()