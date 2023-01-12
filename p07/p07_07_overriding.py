'''
파일명 : p07_07_overriding.py
설 명 : 오버라이딩 (overriding) : 상속관계에서 아버지의 메서드를 재정의
생성일 : 2023/01/12
생성자 : yanghanna
'''
class Person:
    def greeting(self):
        print("안녕하세요")

class Student(Person):
    def greeting(self):
        # parent에 있는 메서드 greeting() 호출
        super().greeting()
        print("hi. 파이썬을 배우는 학생입니다.")

def main():
    stud01 = Student()
    # hi. 파이썬을 배우는 학생입니다.
    stud01.greeting()




main()
