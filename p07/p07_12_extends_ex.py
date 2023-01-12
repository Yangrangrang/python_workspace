'''
파일명 : p07_11_extends_ex.py
설 명 : 
생성일 : 2023/01/12
생성자 : yanghanna
div 오버라이딩 하기 0으로 나눌수 없다.
'''

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def mul(self):
        return self.num1 * self.num2

    def sub(self):
        return self.num1 - self.num2

    def div(self):
        return self.num1 / self.num2

class MoreCalc(Calculator):
    def pow(self):
        return self.num1 ** self.num2

    # div 오버라이딩
    def div(self):
        if self.num2 == 0:
            print('0으로 나눌 수 없습니다.')
            return 0
        else:
            return self.num1 / self.num2

def main():
    a = MoreCalc(4,0)
    # ZeroDivisionError: division by zero : div 오버라이딩 수행
    print(a.div())


main()
