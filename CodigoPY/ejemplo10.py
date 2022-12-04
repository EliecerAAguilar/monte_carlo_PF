import random
import pandas as pd


def pennysgame(p1choice, p2choice):
    
    coinOptions = ['T', 'H']
    coin = []
    #Simulamos los primeros 3 lanzamientos
    for i in range(3): 
        coin.append(coinOptions[random.randint(0,1)])

    doo = True
    while(doo):
        if(list(p1choice) == coin):
            doo = False
            return 1
        elif (list(p2choice) == coin):
            doo = False
            return 0
        else: 
            coin = coin[1:]
            coin.append(coinOptions[random.randint(0,1)])

def games(n):
    choices = ['TTT', 'TTH', 'THT', 'THH', 'HTT', 'HTH', 'HHT', 'HHH'] #H: Cara | T: Sello
    tableWins = []
    for choice1 in choices:
        Semiwins = {}
        for choice2 in choices:
            wins = 0
            if choice1 != choice2: 
                p1choice = choice1
                p2choice = choice2 
                #Se crea la siguiente condicion para que no se repitan los n gramas.
                for i in range(n): 
                    vic = pennysgame(p1choice, p2choice)
                    if vic == 1: 
                        wins +=  1
                Semiwins[''.join(choice1)+'/'+''.join(choice2)] = wins
            else:
                Semiwins[''.join(choice1)+'/'+''.join(choice2)] = 0
        tableWins.append(Semiwins)
    return tableWins

def present(wins, n):
    choices = ['TTT', 'TTH', 'THT', 'THH', 'HTT', 'HTH', 'HHT', 'HHH'] #H: Cara | T: Sello
    data = []
    for group in wins:
        dataElem = []
        for value in group.values():
            dataElem.append(value/n)
        data.append(dataElem)
    df = pd.DataFrame(data, columns=choices, index=choices)
    print('Probabilidades de victoria del jugador 1 (filas: 3-grama de 1 | columnas: 3-grama de 2)')
    print(df)



def run():
    n = int(input('Ingresa la cantidad de juegos que deseas simular (mayor a 1000): ')) #Cantidad de juegos
    wins = games(n) #Diccionarion de ganadas de cada uno
    present(wins,n)


run()