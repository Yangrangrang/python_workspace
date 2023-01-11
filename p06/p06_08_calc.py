'''

'''

class Calculator:
    def setdata(self,first,second):
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

class Calc:
    def data(self,fir,sec):
        self.__fir = fir
        self.__sec = sec

    def add(self):
        return self.__fir + self.__sec

def main():
    calc01 = Calculator()
    calc01.setdata(11,13)
    print(calc01.add())

    calc02 = Calc()
    calc02.data(1,2)
    print(calc02.add())

    # setdata호출 없이 사용 시 오류 발생
    # 'Calculator' object has no attribute 'first'
    # calc03 = Calculator()
    # calc03.add()


main()
