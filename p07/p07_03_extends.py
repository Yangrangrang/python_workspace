'''
파일명 : p07_03_extends.py
설 명 : 
생성일 : 2023/01/12
생성자 : yanghanna
'''
class Person:
    def greeting(self):
        print("안녕하세요.")

class Student(Person):
    def study(self):
        print("공부하기!")

def main():
    s01 = Student()
    s01.greeting()  # parent 메서드 호출
    s01.study()     # Student 메서드 호출

    print(issubclass(Student,Person))   # True

main()
'''
안녕하세요.
공부하기!
'''
