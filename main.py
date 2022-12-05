from CodigoPY.menu import Menu

def main() -> None:
    """script principal para la ejecucion de los ejemplos de Monte carlo como proyecto final de Modelado"""
    try:
        menu = Menu()
        menu.menu_principal()
    except Exception as e:
        print(e.args)


if __name__ == '__main__':
    main()
