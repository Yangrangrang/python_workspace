'''
파일명 : p07_05_member_instance.py
설 명 : 
생성일 : 2023/01/12
생성자 : yanghanna
'''

class Person:
    def __init__(self):
        print("Person __init__")
        self.hello = "안녕하세요"


class Student(Person):
    def __init__(self):
        print("Student __init__")
        super().__init__()  # super로 Person의 __init__메서드 호출 # Person의 hello 인스턴스 변수가 생성됨
        self.school = 'python lab4'

def main():
    stud01 = Student()
    print(stud01.hello) # AttributeError: 'Student' object has no attribute 'hello'
                        # Parant에 __init__이 호출되지 않았기 때문에
                        # 해결은 super
    print(stud01.school)



main()
