'''
    리스트는 시퀀스 데이터 타입이기 때문에 인덱스를 이용해서 접근 할 수 있다.
    인덱스의 시작 번지는 '0'번 부터 시작하게 된다.
'''


def main():

    # 리스트 인덱싱
    # 길이가 8인 인덱스
    a = [11, 13, 16, 46, 51, 'a', 'b', 'c']

    # 인자 접근
    print('a[0]:{}'.format(a[0]))
    print('a[2]:{}'.format(a[2]))

    # 마이너스
    print('a[-1]:{}'.format(a[-1]))

main()