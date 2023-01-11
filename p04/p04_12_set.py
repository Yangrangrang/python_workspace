'''

'''


def main():
    s1 = set([1,2,3,4,5,6])
    s2 = set([4,5,6,7,8,9])

    #4,5,6이 중복됨

    # 교집합 : &
    print('s1 & s2:{}'.format(s1 & s2)) # s1 & s2:{4, 5, 6}
    print('s1.intersection(s2):{}'.format(s1.intersection(s2)))

    # 합집합 : |, 중복된 데이터는 하나만 출력
    # s1 | s2 :{1, 2, 3, 4, 5, 6, 7, 8, 9}
    print('s1 | s2 :{}'.format(s1 | s2))
    print('s1.union(s2):{}'.format(s1.union(s2)))

    # 차집합 : -
    # s1 - s2 :{1, 2, 3}
    print('s1 - s2 :{}'.format(s1 - s2))
    print('s1.difference(s2) :{}'.format(s1.difference(s2)))

main()
'''
s1 & s2:{4, 5, 6}
s1.intersection(s2):{4, 5, 6}
s1 | s2 :{1, 2, 3, 4, 5, 6, 7, 8, 9}
s1.union(s2):{1, 2, 3, 4, 5, 6, 7, 8, 9}
s1 - s2 :{1, 2, 3}
s1.difference(s2) :{1, 2, 3}
'''
