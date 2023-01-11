'''
튜플 인덱싱
'''


def main():
    t1 = ('a', 'b', 'c', 10, 9, 8)
    print('t1:{}'.format(t1))

    # 튜플의 인덱스
    print(f't1[0]: {t1[0]}')    # t1[0]: a
    print('t1[1]:{}'.format(t1[1]))

    # 튜플의 인덱스 범위를 넘어감
    # tuple index out of range
    # print('t1[7]:{}'.format(t1[7]))

    # 튜플 슬라이싱
    # t1[1:]:('b', 'c', 10, 9, 8)
    print('t1[1:]:{}'.format(t1[1:]))

    # 튜플 더하기
    # t1+t2:('a', 'b', 'c', 10, 9, 8, 88, 77, 99)
    t2 = (88, 77, 99)
    print('t1+t2:{}'.format(t1+t2))

    # 튜플 곱하기
    # t2*3:(88, 77, 99, 88, 77, 99, 88, 77, 99)
    print('t2*3:{}'.format(t2 * 3))

    # 튜플 길이 구하기 : len()
    # 3
    print(len(t2))

    # (1,2,3)튜플에 4를 넣어 출력
    # 소가로를 생략해도 튜플임
    a = 1, 2, 3 # 가로를 생략해도 된다.
    print('a:{}, type(a):{}'.format(a, type(a)))
    # b = (4,)
    # print(a + b)
    print(a + (4,))



main()
