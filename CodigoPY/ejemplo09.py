import random
import math

def singlecrap():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    sum1 = dice1 + dice2
    if (sum1 == 7 or sum1 == 11):  #Condicion de victoria en la primera tirada
        return 1
    elif (sum1 == 2 or sum1 == 3 or sum1 == 12):  #Condicion de perdida en la primera tirada
        return 0
    else: #Condicion de seguir tirando dados.
        foo = True
        while(foo):
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            sum2 = dice1 + dice2
            if(sum2 == sum1):
                foo = False
                return 1
            elif(sum2==7):
                foo = False
                return 0 



def crap(n):
    wins = 0
    for i in range(n):
        wins = wins + singlecrap()
    return wins

def run(): 
    #Numero de repeticiones del juego
    pTeorica = 0.49228 #Probabilidad real de ganar el juego 
    n =  int(input('Cuantas veces desea correr el juego (Preferiblemente mas de 10 000): '))
    wins = crap(n)
    pExperimental = wins/n #Probabilidad experimental(simulada) de ganar el juego
    error = abs((pExperimental-pTeorica)/pTeorica) *100
    print('La probabilidad de ganar el juego es: {}'.format(pExperimental))
    print('Teoricamente esta probabilidad es de {0} donde comparando con la Simulacion tenemos un error de {1:.4f}%'.format(pTeorica, error))

run()