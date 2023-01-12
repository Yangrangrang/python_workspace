'''
파일명 : p07_01_setter_getter.py
설 명 : setter,getter
생성일 : 2023/01/12
생성자 : yanghanna
'''

class Person:
    def __init__(self):
        self.__name = ""

    @property   # getter
    def name(self):
        return self.__name

    @name.setter    # setter
    def name(self,text):
        self.__name = text

def main():
    p01 = Person()
    p01.name = "홍"  # setter에 값 할당
    print(p01.name)   # getter로 값 가져오기


main()
