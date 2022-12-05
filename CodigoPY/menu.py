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
        print("Seleccione el Ejemplo a ejecutar:")
        for clave, valor in opciones.items():
            print(f' {clave}: {valor[0]}')

    def leer_opcion(self, opciones: dict) -> str:
        while (opcion := input('Opción: ')) not in opciones:
            print('Opción incorrecta, vuelva a intentarlo.')
        return opcion

    def ejecutar_opcion(self, opcion: str, opciones: dict) -> None:
        opciones[opcion][1]()

    def generar_menu(self, opciones: dict, opcion_salida: str) -> None:
        opcion: str = ""
        while opcion != opcion_salida:
            self.mostrar_menu(opciones)
            opcion = self.leer_opcion(opciones)
            self.ejecutar_opcion(opcion, opciones)
            print("#"*80)
        system("cls")

    def menu_principal(self) -> None:
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
        print('Has elegido ejecutar el Ejemplo #1: ')
        ejemplo01= Ejemplo01()
        ejemplo01.run()

    def ejemplo2(self) -> None:
        print('Has elegido ejecutar el Ejemplo #2: ')
        ejemplo02 = Ejemplo02()
        ejemplo02.run()

    def ejemplo3(self) -> None:
        print('Has elegido ejecutar el Ejemplo #3: ')
    def ejemplo4(self) -> None:
        print('Has elegido ejecutar el Ejemplo #4: ')
    def ejemplo5(self) -> None:
        print('Has elegido ejecutar el Ejemplo #5: ')
    def ejemplo6(self) -> None:
        print('Has elegido ejecutar el Ejemplo #6: ')
    def ejemplo7(self) -> None:
        print('Has elegido ejecutar el Ejemplo #7: ')
    def ejemplo8(self) -> None:
        print('Has elegido ejecutar el Ejemplo #8: ')
    def ejemplo9(self) -> None:
        print('Has elegido ejecutar el Ejemplo #9: ')
    def ejemplo10(self) -> None:
        print('Has elegido ejecutar el Ejemplo #1: 0')
    def salir(self):
        print('Saliendo')
