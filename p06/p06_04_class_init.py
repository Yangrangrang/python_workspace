'''

'''

class Person:
    def __init__(self, *args):# 가변 파라미터 name,age,address
        self.hello = '안녕하세요'
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]

    def greeting(self):
        print("{0} 저는 {1}입니다.".format(self.hello, self.name))

def main():
    #  파람 객체 생성하면서 전달
    kim = Person(*['Kim', '23', '서울시 마포구'])

    # 메서드
    kim.greeting()

    print('이름:', kim.name)
    print('나이:', kim.age)
    print('주소:', kim.address)


main()
