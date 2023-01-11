'''

'''

class Calculator:
    def __init__(self,first,second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result



def main():

    calc01 = Calculator(11,13)
    print('calc01:{}'.format(calc01))
    print('calc01.add:{}'.format(calc01.add()))

    # setdata호출 없이 사용시 오류발생
    calc02 = Calculator(1,2)
    print(calc02.add())


main()
