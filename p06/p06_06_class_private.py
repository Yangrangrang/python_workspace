'''

'''

class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet  # 변수 앞에 __를 붙여서 비공개 속성으로 생성

    def pay(self,amount):
        if amount > self.__wallet:  # 사용하려고 하는 금액보다 지갑에 든 돈이 적을 때
            print('잔고를 확인하세요.')
        return

        self.__wallet -= amount # 비공개 속성은 클래스안의 메서드를 통해 접근할 수 있음
        print('이제 {0}원 남았네요.'.format(self.__wallet))

def main():
    james = Person('제임스', '23', '서울시 마포구',100000000)
    print(james.name)
    # james.__wallet -= 100   # 클래스 바깥에서 접근하면 에러가 발생

    james.pay(1000000)      # 이제 99000000원 남았네요.

    james.pay(100000000)

main()
