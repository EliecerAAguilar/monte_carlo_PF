from CodigoPY.ejemplo01 import Ejemplo01
from CodigoPY.ejemplo02 import Ejemplo02
from CodigoPY.ejemplo03 import Ejemplo03
from CodigoPY.ejemplo04 import Ejemplo04
from CodigoPY.ejemplo05 import Ejemplo05
from CodigoPY.ejemplo06 import Ejemplo06
from CodigoPY.ejemplo07 import Ejemplo07
from CodigoPY.ejemplo08 import Ejemplo08
from CodigoPY.ejemplo09 import Ejemplo09
from CodigoPY.ejemplo10 import Ejemplo10



def main():
    try:
        ejemplo01 = Ejemplo01()
        ejemplo01.run()

        ejemplo02 = Ejemplo02()
        ejemplo02.run()

    except Exception as e:
        print(e.args)


if __name__ == '__main__':
    main()
