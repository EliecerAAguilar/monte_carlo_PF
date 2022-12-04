from tabulate import tabulate
import math
import random

def borracho(n):
    data = []
    x=0
    y=0
    for i in range(n):
        r=random.uniform(0,100)
        if(r>=0 and r<25):
            y+=1
        if(r>=25 and r<50):
            y-=1
        if(r>=50 and r<75):
            x+=1
        if(r>=75 and r<100):
            x-=1

        data.append((i,r,x,y))

    present(data)
    
    if(abs(x)+abs(y)>=2):
        print("El borracho termino a 2 o mas cuadras de donde estaba inicialmente.")
    else:
        print("El borracho termino a menos de 2 cuadras de donde estaba inicialmente.")


def present(data):
    headers = [ '# Cuadras',
                '# Aleatorio', 
                'Loc. X',
                'Loc. Y',
                ]

    print(tabulate(data, headers=headers, showindex=False))



def main():
    #Lectura de datos
    print('SIMULACION DEL TAMBALEO DEL BORRACHO')
    n = int(input('Cual es el valor de n: '))
    print('-------------------------')
    borracho(n)

main()