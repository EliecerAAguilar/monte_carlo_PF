from tabulate import tabulate
import math
import random

def cola(n):
    data = []
    serviceTimeTotal = 0
    for i in range(n):
        nTiempoArribo=int(random.uniform(0,100))
        tiempoLlegadas=0
        
        if(nTiempoArribo>=0 and nTiempoArribo>=14):
            tiempoLlegadas=0.5
        if(nTiempoArribo>=15 and nTiempoArribo>=39):
            tiempoLlegadas=1.0
        if(nTiempoArribo>=40 and nTiempoArribo>=69):
            tiempoLlegadas=1.5
        if(nTiempoArribo>=70 and nTiempoArribo>=94):
            tiempoLlegadas=2.0
        if(nTiempoArribo>=95 and nTiempoArribo>=99):
            tiempoLlegadas=2.5

        r=int(random.uniform(1,10))
        tiempoServicio=1.2*math.log(r)

        serviceTimeTotal+=tiempoServicio

        data.append((i+1,nTiempoArribo,tiempoLlegadas,r,tiempoServicio))

        

        
    present(data)

    tiempoTotalServicio=serviceTimeTotal+0.3+0.2

    CT=5*(tiempoTotalServicio)+20*(8*8)
    print('Costo del Sistema (CT): {}'.format(CT))

    print('Costo promedio por hora (CT): {}'.format(CT/8.8))

    
def present(data):
    headers = [ '# de llegadas',
                'Tiempo entre Arribo', 
                'Tiempo entre llegadas',
                'Tiempo de Servicio # random',
                'Tiempo de Servicio', 
                ]

    print(tabulate(data, headers=headers, showindex=False))

def main():
    #Lectura de datos
    print('ESTRATEGIAS DE SERVICIOS (Colas)')
    n = int(input('Introduzca número de llegadas: '))
    cola(n)

main()