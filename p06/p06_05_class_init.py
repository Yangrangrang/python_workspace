'''

'''

class Person:
    def __init__(self, **kwargs):# 가변 파라미터 name,age,address
        self.hello = '안녕하세요'
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']

    def greeting(self):
        print("{0} 저는 {1}입니다.".format(self.hello, self.name))

def main():
    #  파람 객체 생성하면서 전달
    # kim = Person(name='Kim', age=23, address='서울시 마포구')
    kim = Person( **{'name':'Kim', 'age':23, 'address':'서울시 마포구'})


    # 메서드
    kim.greeting()

    print('이름:', kim.name)
    print('나이:', kim.age)
    print('주소:', kim.address)


main()
