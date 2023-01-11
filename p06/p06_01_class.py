'''

'''
class Person:
    def greeting(self): # self는 첫번째 인자로 무조건 붙는다.(메소드의 첫번째 매개변수는 반드시 self를 지정해야한다.)
        print("Hello")

def main():
    # 인스턴스 생성
    # 인스턴스 = 클래스()
    p01 = Person()
    p01.greeting()


main()
