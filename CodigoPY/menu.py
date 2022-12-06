from CodigoPY.ejemplo01 import Ejemplo01
from CodigoPY.ejemplo02 import Ejemplo02
from os import system
class Menu:
    """
    Clase Menu
    Esta clase es para la creacion y manejo de las opciones y funciones
    que presentara un menu de opciones segun entrada del desarrollador
    """

    def mostrar_menu(self, opciones: dict) -> None:
        """impreme los valores del menu deseado en pantalla por consola
        :param opciones: diccionario con las opciones a imprimir
        :type opciones: dict
        :return este metodo no retorna ningun valor
        :rtype None
        """
        print("Seleccione el Ejemplo a ejecutar:")
        for clave, valor in opciones.items():
            print(f' {clave}: {valor[0]}')

    def leer_opcion(self, opciones: dict) -> str:
        """
        lee la opcion que el usuario escoge por medio del teclado
        :param opciones: opciones a escoger
        :type opciones: dict
        :return: el valor que fue escogido
        :rtype str
        """
        while (opcion := input('Opción: ')) not in opciones:
            print('Opción incorrecta, vuelva a intentarlo.')
        return opcion

    def ejecutar_opcion(self, opcion: str, opciones: dict) -> None:
        """
        metodo para ejecutar la opcion que halla escogido el usuario
        :param opcion: opcion escogida por el usuario desde el menu en la consola por medio del teclado
        :type: opcion: str
        :param opciones: diccionario con las opciones para escoger en el menu
        :type: opciones: dict
        :return: nada
        :rtype: None
        """
        opciones[opcion][1]()

    def generar_menu(self, opciones: dict, opcion_salida: str) -> None:
        """
        metodo para generar el menu de opciones, donde el usuario introducira los valores deseados
        :param opciones: diccionario con los valores del menu
        :type opciones: dict
        :param opcion_salida:
        :type opcion_salida: str
        :return: Nada
        :rtype: None
        """
        opcion: str = ""
        while opcion != opcion_salida:
            system("cls")
            print("#"*80)
            self.mostrar_menu(opciones)
            opcion = self.leer_opcion(opciones)
            self.ejecutar_opcion(opcion, opciones)


    def menu_principal(self) -> None:
        """
        Metodo para correr el menu
        :return: nada
        :rtype None
        """
        opciones: dict = {
            '1': ('Ejemplo 1', self.ejemplo1),
            '2': ('Ejemplo 2', self.ejemplo2),
            '3': ('Ejemplo 3', self.ejemplo3),
            '4': ('Ejemplo 4', self.ejemplo4),
            '5': ('Ejemplo 5', self.ejemplo5),
            '6': ('Ejemplo 6', self.ejemplo6),
            '7': ('Ejemplo 7', self.ejemplo7),
            '8': ('Ejemplo 8', self.ejemplo8),
            '9': ('Ejemplo 9', self.ejemplo9),
            '10': ('Ejemplo 10', self.ejemplo10),
            '11': ('Salir', self.salir)
        }

        self.generar_menu(opciones, '11')

    def ejemplo1(self) -> None:
        """
        metodo para ejecutar el Ejemplo #1
        :return: nada
        :rtype None
        """
        print('Has elegido ejecutar el Ejemplo #1: ')
        ejemplo01= Ejemplo01()
        ejemplo01.run()

    def ejemplo2(self) -> None:
        """
        metodo para ejecutar el Ejemplo #02
        :return: nada
        :rtype None
        """
        print('Has elegido ejecutar el Ejemplo #2: ')
        ejemplo02 = Ejemplo02()
        ejemplo02.run()


    def ejemplo3(self) -> None:
        """
        metodo para ejecutar el Ejemplo #03
        :return: nada
        :rtype None
        """
        print('Has elegido ejecutar el Ejemplo #3: ')

    def ejemplo4(self) -> None:
        """
        metodo para ejecutar el Ejemplo #04
        :return: nada
        :rtype None
        """
        print('Has elegido ejecutar el Ejemplo #4: ')

    def ejemplo5(self) -> None:
        """
        metodo para ejecutar el Ejemplo #05
        :return: nada
        :rtype None
        """
        print('Has elegido ejecutar el Ejemplo #5: ')

    def ejemplo6(self) -> None:
        """
        metodo para ejecutar el Ejemplo #06
        :return: nada
        :rtype None
        """
        print('Has elegido ejecutar el Ejemplo #6: ')

    def ejemplo7(self) -> None:
        """
        metodo para ejecutar el Ejemplo #07
        :return: nada
        :rtype None
        """
        print('Has elegido ejecutar el Ejemplo #7: ')

    def ejemplo8(self) -> None:
        """
        metodo para ejecutar el Ejemplo #08
        :return: nada
        :rtype None
        """
        print('Has elegido ejecutar el Ejemplo #8: ')

    def ejemplo9(self) -> None:
        """
        metodo para ejecutar el Ejemplo #09
        :return: nada
        :rtype None
        """
        print('Has elegido ejecutar el Ejemplo #9: ')

    def ejemplo10(self) -> None:
        """
        metodo para ejecutar el Ejemplo #10
        :return: nada
        :rtype None
        """
        print('Has elegido ejecutar el Ejemplo #10: ')

    def salir(self) -> None:
        """
        metodo para mostrar que se esta saliendo del menu y finaliza el programa
        :return: nada
        :rtype None
        """
        print('Saliendo')