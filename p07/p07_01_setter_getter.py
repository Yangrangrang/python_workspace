'''
파일명 : p07_01_setter_getter.py
설 명 : setter,getter
생성일 : 2023/01/12
생성자 : yanghanna
'''

class Person:
    def __init__(self):
        self.__name = ""

    def name_getter(self):
        return self.__name

    def name_setter(self,text):
        self.__name = text

def main():
    p01 = Person()
    p01.name_setter("Kim")
    print(p01.name_getter())


main()
