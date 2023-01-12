'''
파일명 : p07_09_diamond.py
설 명 : 다이아몬드 상속
생성일 : 2023/01/12
생성자 : yanghanna
'''
class A:
    def greeting(self):
        print("A 안녕하세요")

class B(A):
    def greeting(self):
        print("B 안녕하세요")

class C(A):
    def greeting(self):
        print("C 안녕하세요")

class D(B,C):
    pass

def main():
    x = D()
    x.greeting()

    # 메서드 탐색 순서 확인 (Method Resolution Order : MRO)
    print(D.mro())


main()
