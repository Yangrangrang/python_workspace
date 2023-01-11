'''

'''

class Person:
    def __init__(self,name,age,address):
        self.hello = '안녕하세요'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print("{0} 저는 {1}입니다.".format(self.hello, self.name))

def main():
    #  파람 객체 생성하면서 전달
    kim = Person('Kim', '23', '서울시 마포구')

    # 메서드
    kim.greeting()

    print('이름:', kim.name)
    print('나이:', kim.age)
    print('주소:', kim.address)


main()
