'''
파일명 : p07_08_extends.py
설 명 : 다중 상속
생성일 : 2023/01/12
생성자 : yanghanna
'''

class Person:
    def greeting(self):
        print("안녕하세요")

class University:
    def manager_credit(self):
        print("학점관리")

class Undergraduate(Person, University):
    def study(self):
        print("공부하기")

def main():
    james = Undergraduate()
    james.greeting()        # Person 메서드 호출
    james.manager_credit()  # University 메서드 호출
    james.study()           # Undergraduate에서 추가한 메서드 호출


main()
'''
안녕하세요
학점관리
공부하기
'''
