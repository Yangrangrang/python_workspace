'''
    집합 자료형
'''


def main():
    s1 = set([1,2,3])
    # s1:{1, 2, 3},type(s1):<class 'set'>
    print('s1:{},type(s1):{}'.format(s1, type(s1)))

    s2 = set("Hello")
    # s2:{'l', 'e', 'H', 'o'}
    # 중복 데이터 불허
    # 순서 보장 안됨
    print('s2:{}'.format(s2))


main()
