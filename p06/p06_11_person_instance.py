'''

'''

class Person:
    # 클래스 속성
    def __init__(self): # 생성자: 인스턴스 속성 bag
        self.bag = []


    def put_bag(self,stuff):
        self.bag.append(stuff)    # 클래스이름.변수명

def main():
    mari = Person()
    mari.put_bag("책")

    james = Person()
    james.put_bag("키")

    print(mari.bag)
    print(james.bag)

main()
