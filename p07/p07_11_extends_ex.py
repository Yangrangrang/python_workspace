'''
파일명 : p07_11_extends_ex.py
설 명 : 
생성일 : 2023/01/12
생성자 : yanghanna
pow = a 의 제곱을 계산하는 프로그램을 작성해 봅시다.
a = MoreCalc(4,2)
a.pow()
>> 16
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

def main():
    a = MoreCalc(4,2)
    print('a.pow:{}'.format(a.pow()))
    print(a.add())


main()
