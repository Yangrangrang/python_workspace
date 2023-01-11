'''
    딕셔너리 전체 데이터 출력
'''


def main():
    d = {'a':123321, 'kim':'pacmk', 'b':'blog', 'c':333,123:'name'}

    # 키 값 출력
    print(d.keys()) # dict_keys(['a', 'kim', 'b', 'c', 123])

    # key 하나씩 받기
    for k in d.keys():
        print('k:{}'.format(k))


main()
