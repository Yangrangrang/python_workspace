'''
파일명 : p07_05_member_instance.py
설 명 : super().__init__() 생략
생성일 : 2023/01/12
생성자 : yanghanna
'''

class Person:
    def __init__(self):
        print("Person __init__")
        self.hello = "안녕하세요"


class Student(Person):  # Parent의 __init__이 자동 호출
    pass

def main():
    stud01 = Student()
    print(stud01.hello)



main()
