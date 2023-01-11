'''

'''


def main():
    s1 = set([1,2,3])
    print('s1:{}'.format(s1))           # s1:{1, 2, 3}

    # 리스트로 변환
    list01 = list(s1)
    print('list01:{}, type(s1):{}'.format(list01, type(s1)))   # list01:[1, 2, 3], type(s1):<class 'set'>

    # 튜플로 변환
    t1 = tuple(s1)
    print('t1:{}, type(t1):{}'.format(t1, type(t1)))           # t1:(1, 2, 3), type(t1):<class 'tuple'>

main()
