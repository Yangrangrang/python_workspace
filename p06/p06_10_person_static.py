'''

'''

class Person:
    # 클래스 속성
    bag = []    # java로 치면 static 변수

    def put_bag(self,stuff):
        Person.bag.append(stuff)    # 클래스이름.변수명
        # self.bag.append(stuff)

def main():
    mari = Person()
    mari.put_bag("책")

    print(mari.bag)

    james = Person()
    james.put_bag("키")

    print(mari.bag)
    print(james.bag)
    print('Person.bag:{}'.format(Person.bag))   # Person.bag:['책', '키']

    # 클래스 변수 확인
    print(Person.__dict__)

    print('james.__dict__:{}'.format(james.__dict__))
main()
