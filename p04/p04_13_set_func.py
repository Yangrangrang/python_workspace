'''

'''


def main():
    s = {1, 2, 3}
    # s:{1, 2, 3}, type(s):<class 'set'>
    print('s:{}, type(s):{}'.format(s, type(s)))

    # 추가
    s.add('pcmk')
    print('s:{}'.format(s))

    # 중복된 값 추가
    s.add('pcmk')
    print('s:{}'.format(s))

    s.add(4)
    print('s:{}'.format(s))

    # 여러개 추가
    s.update([11,22,33])
    print('s:{}'.format(s))

main()
