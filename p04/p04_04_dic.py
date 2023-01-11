'''

'''


def main():
    d = {'a':123321}

    # 값 추가
    d[999] = 10     # 숫자 키, 숫자 값
    d['999'] = 111  # 문자 키, 숫자 값
    d['mask'] = 'blog'  # 문자 키, 문자 값

    # 리스트 값 추가
    d['wow'] = [1,2,3,4,5]
    d[1] = (3, 'a', 5)

    # 값 접근
    print("딕셔너리 값 접근")
    print('d[a]:{}'.format(d['a']))     # d[a]:123321
    print('d[wow]:{}'.format(d['wow'])) # d[wow]:[1, 2, 3, 4, 5]
    print('d[1]:{}'.format(d[1]))       # d[1]:(3, 'a', 5)

    # 값 변경
    print("딕셔너리 값 변경")
    print('before:d[mask]:{}'.format(d['mask']))
    d['mask'] = 'cafe'
    print('before:d[mask]:{}'.format(d['mask']))

    # d:{'a': 123321, 999: 10, '999': 111, 'mask': 'cafe', 'wow': [1, 2, 3, 4, 5], 1: (3, 'a', 5)}
    print('d:{}'.format(d))

    # 값 삭제
    del d[1]
    print('d:{}'.format(d))


main()
