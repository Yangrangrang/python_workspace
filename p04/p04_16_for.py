'''

'''


def main():
    t_list = ['one', 'two', 'three']
    # 리스트 for
    for i in t_list:
        print(i)

    # 문자열
    for s in 'abcdef':
        print('s:{},{}'.format(s, ord(s)))

    # 순차적으로 숫자를 반복하는 경우 range() 함수를 사용한다.
    print(range(10))    # 0 <= x < 10
    print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for x in range(10):
        print(x, end=", ")  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,

main()
