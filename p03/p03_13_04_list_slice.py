'''

'''


def main():
    a = [11, 13, 16, 46, 51, 'a', 'b', 'c']
    print('a:{}'.format(a))

    print('a[1:4]:{}'.format(a[1:4]))   # a[1:4]:[13, 16, 46]

    print('a[:4]:{}'.format(a[:4])) # 0번지 부터 시작 a[:4]:[11, 13, 16, 46]

    # a[4:]:[51, 'a', 'b', 'c']
    print('a[4:]:{}'.format(a[4:])) # 4번지 부터 끝까지

    print('a[:]:{}'.format(a[:]))   # 전체 데이터 출력

    w = len(a);
    print('w:{}'.format(w))

    print('a[:w]:{}'.format(a[:w]))

    print('a[:-1]:{}'.format(a[:-1]))




main()
