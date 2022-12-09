import random
import pandas as pd
from typing import List

class Ejemplo10:
    """Clase para el Ejemplo #10"""
    def pennysgame(self, p1choice: str, p2choice: str) -> int:

        coin_options = ['T', 'H']

        coin: List[str] = []
        for _ in range(3):
            coin.append(coin_options[random.randint(0, 1)])

        for _ in range(100):
            if coin == list(p1choice):
                return 1
            elif coin == list(p2choice):
                return 0
            else:
                coin = coin[1:]
                coin.append(coin_options[random.randint(0, 1)])
        # condicion de empate
        return -1

    def games(self, n: int) -> List[dict]:
        """
        metodo para ejecutar el juego
        :param n: cantidad de veces a ejecutar el juego
        :return: lista de diccionarios con los ganadores
        :rtype List[dict]
        """
        choices: List[str] = ['TTT', 'TTH', 'THT', 'THH', 'HTT', 'HTH', 'HHT', 'HHH'] #H: Cara | T: Sello
        tableWins: List[dict] = []
        for choice1 in choices:
            Semiwins: dict = {}
            for choice2 in choices:
                wins = 0
                if choice1 != choice2:
                    p1choice: str = choice1
                    p2choice: str = choice2
                    #Se crea la siguiente condicion para que no se repitan los n gramas.
                    for i in range(n):
                        vic = self.pennysgame(p1choice, p2choice)
                        if vic == 1:
                            wins +=  1
                    Semiwins[''.join(choice1)+'/'+''.join(choice2)] = wins
                else:
                    Semiwins[''.join(choice1)+'/'+''.join(choice2)] = 0
            tableWins.append(Semiwins)
        return tableWins

    def present(self, wins: List[dict], n: int) -> None:
        """
        Metodo para imprimir en pantalla los valores de la simulacion del juego
        :param wins: lista de diccionarios con la cantidad de veces que gana cada jugador
        :type wins: List[dict]
        :param n: cantidad de veces a simular este juego
        :type n: int
        :return:
        """
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

    def run(self) -> None:
        """
        Metodo para ejecutar la simulacion del juego de penny
        :return: Nada
        :rtype None
        """
        n: int = int(input('Ingresa la cantidad de juegos que deseas simular (mayor a 1000): ')) #Cantidad de juegos
        wins:List[dict] = self.games(n) #Diccionarion de ganadas de cada uno
        self.present(wins,n)
