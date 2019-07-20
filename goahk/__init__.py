#! python3
from .main import goahk, getahk


def test():
    goahk(u'''msgbox Hello World
    msgbox From Pyld
    pyld=12345
    ''')
    print(getahk(u'pyld'))
    print(111)


if __name__ == "__main__":
    test()
