'''

'''


def main():
    b = [11, 13, 16]

    print('b:{}'.format(b)) # b:[11, 13, 16]

    b[0] = 9
    # 값 변경
    print('b:{}'.format(b)) # b:[9, 13, 16]

    b[-1] = '오늘은 즐거운 수요일'
    print('b:{}'.format(b)) # b:[9, 13, '오늘은 즐거운 수요일']

    # List 내에 List
    a = [1, 2, 3, ['a', 'b', 'c']]
    print(a)

    print('a[0]:{}'.format(a[0]))

    print('a[3]:{}'.format(a[3]))   # a[3]:['a', 'b', 'c']

    print('a[-1]:{}'.format(a[-1]))
    print('a[-1][1]:{}'.format(a[-1][1]))    # a[-1][1]:b


main()
