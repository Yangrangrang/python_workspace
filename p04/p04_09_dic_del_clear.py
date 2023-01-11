'''

'''


def main():
    d = {'a': 123321, 'kim': 'pacmk', 'b': 'blog', 'c': 333, 123: 'name'}
    print('before: d:{}'.format(d))
    del d['a']
    del d['b']
    # del d['b99']  # KeyError: 'b99' : key 없음
    print('after: d:{}'.format(d))

    # 딕셔너리에 key 존재 여부 확인
    print('c' in d) # True
    print('c99' in d)  # False

    # 전체 삭제
    d.clear()
    print('clear: d:{}'.format(d))  # clear: d:{}


main()
