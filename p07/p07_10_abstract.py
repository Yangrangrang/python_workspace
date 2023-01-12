'''
파일명 : p07_10_abstract.py
설 명 : 
생성일 : 2023/01/12
생성자 : yanghanna
'''

from abc import *

class StudentBase(metaclass=ABCMeta):
    @abstractclassmethod
    def study(self):
        pass

    @abstractclassmethod
    def go_to_school(self):
        pass

# 추상클래스를 상속 받으면 : 상위 클래스의 추상 메서드를
# 모두 오버라이딩 해야한다.
class Student(StudentBase):
    def study(self):
        print("공부하기")

    def go_to_school(self):
        print("학교가기")

def main():
    stud01 = Student()
    stud01.study()

    # 추상클래스는 객체를 스스로 만들 수 없고, 상속 받은 하위 클래스에서 부모 추상메서드를 모두 오버라이딩 하고 객체를 생성한다.
    base = StudentBase()

    # TypeError: Can't instantiate abstract class Student with abstract method go_to_school
    # 메서드 재정의를 하지 않아서 (Student에서 go_to_school를 아직 재정의 안했을 떄 run 한 상태)

    base = StudentBase()



main()
