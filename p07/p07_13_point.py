'''
파일명 : p07_13_point.py
설 명 : 두 점 사이의 거리 구하기
생성일 : 2023/01/12
생성자 : yanghanna
'''
import math


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def main():
    p01 = Point(30,20)
    p02 = Point(60,50)

    # 두 점
    a = p02.x - p01.x   # 밑변
    b = p02.y - p01.y   # 높이

    # c = math.sqrt( (a*a) + (b*b) )
    c  = ((a * a) + (b * b) ** 0.5)

    print('c:{}'.format(c))


main()
