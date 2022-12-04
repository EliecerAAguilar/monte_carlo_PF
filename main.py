from CodigoPY.ejemplo01 import Ejemplo01


def main():
    try:
        ejemplo01 = Ejemplo01()
        ejemplo01.run()
    except Exception as e:
        print(e.args)


if __name__ == '__main__':
    main()
