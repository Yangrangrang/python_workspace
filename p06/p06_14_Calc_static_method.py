'''

'''

class Calculator:
    @staticmethod
    def add(a, b):
        print(a + b)

    @staticmethod
    def mul(a, b):
        print(a * b)

def main():
    Calculator.add(1, 4)    # 클래스에서 바로 메서드 호출
    Calculator.mul(1, 4)    # 클래스에서 바로 메서드 호출


main()
