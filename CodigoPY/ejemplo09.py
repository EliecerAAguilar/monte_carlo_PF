import random


class Ejemplo09:
    """Clase para el desarrollo del Ejemplo #9"""
    def singlecrap(self) -> int:
        """
        Metodo para verificar las condiciones de victoria y perdida
        :return: valor entero que verifica la victoria o derrota
        :rtype int
        """

        condicion = {
            7: 1,  # Winning condition
            11: 1,  # Winning condition
            2: 0,  # Losing condition
            3: 0,  # Losing condition
            12: 0  # Losing condition
        }

        dice_roll_1 = random.randint(1, 6)
        dice_roll_2 = random.randint(1, 6)


        sum1 = dice_roll_1 + dice_roll_2

        # verificar la condicion de victorio o perdida en la primera tirada de dados
        if sum1 in condicion:
            return condicion[sum1]

        # seguir tirando los dados si la condicion de victoria/ derrota no se cumple la primera vez
        for _ in range(100):
            dice_roll_1 = random.randint(1, 6)
            dice_roll_2 = random.randint(1, 6)
            sum2 = dice_roll_1 + dice_roll_2

            if sum2 == sum1:
                return 1
            elif sum2 == 7:
                return 0

        # condicion de empate, en el caso de darse cuando se tiran muchas veces sin alcanzar la condicion
        # de victoria o derrota
        return -1

    def crap(self, n: int) -> int:
        """
        Metodo para la ejecucion de la simulacion
        :param n: cantidad de veces a correr el juego
        :type n: int
        :return: cantidad de veces que gano
        :rtype int
        """
        wins: int = 0
        for i in range(n):
            wins = wins + self.singlecrap()
        return wins

    def run(self) -> None:
        """
        Metodo para ejecutar la simulacion del Ejemplo #9
        :return: Nada
        :rtype None
        """
        pTeorica = 0.49228 #Probabilidad real de ganar el juego
        n: int =  int(input('Cuantas veces desea correr el juego (Preferiblemente mas de 10 000): '))
        wins: int = self.crap(n)
        pExperimental: float = wins/n #Probabilidad experimental(simulada) de ganar el juego
        error: float = abs((pExperimental-pTeorica)/pTeorica) * 100
        print(f'La probabilidad de ganar el juego es: {pExperimental}')
        print(f'Teoricamente esta probabilidad es de {pTeorica} donde comparando con la Simulacion tenemos un error de {error:.4f}%')

