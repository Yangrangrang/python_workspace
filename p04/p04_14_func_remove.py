'''

'''


def main():
    s = {'kim', 'lee', 'park', 2,3,4}
    print('before:{}'.format(s))

    s.remove('kim')
    print('after:{}'.format(s))

    # 집합에 없는 요소 삭제 : KetError 발생
    # s.remove('kim99')   # KeyError: 'kim99'

    # discard : 값이 있으면 삭제, 없으면 아무일도 일어나지 않음
    s.discard('park')
    s.discard('park')
    print('after:{}'.format(s))

    # pop : 임의의 요소를 갖고 온 후 제거
    s.pop()
    print('after:{}'.format(s))
    print(s.pop())
    s.pop()
    s.pop()
    print('after:{}'.format(s)) # after:set()

    # clear : 모든 요소 제거
    s = {'kim', 'lee', 'park', 2, 3, 4}
    print('before:{}'.format(s))
    s.clear()
    print('after:{}'.format(s))

main()
