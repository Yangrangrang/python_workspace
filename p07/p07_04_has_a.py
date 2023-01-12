'''
파일명 : p07_04_has_a.py
설 명 : 포함관계 Composite
생성일 : 2023/01/12
생성자 : yanghanna
'''

class Person:
    def greeting(self):
        print("안녕하세요")

class PersonList:   # has a: PersonList has a Person
    def __init__(self):
        self.person_list = []   # 리스트 속성에 Person을 넣어 관리

    def append_person(self,person): # 리스트 속성에 Person 인스턴스 추가
        self.person_list.append(person)

def main():
    pass


main()
