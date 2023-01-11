'''
    Calculator:
    def __init__(self):
        self.result = 0
    def add(self,num)
'''

class Calculator:
    def __init__(self): # 생성자 선언
        self.reseult = 0  # java로 치면 this와 유사

    def add(self,num):
        # self.num = num
        self.reseult += num

        return self.reseult

def main():
    cal01 = Calculator()

    # 특정 클래스의 인스턴스인지 확인
    print(isinstance(cal01, Calculator))
    print(cal01.add(1))
    print(cal01.add(4))

    cal02 = Calculator()
    print(cal02.add(3))
    print(cal02.add(4))



main()
