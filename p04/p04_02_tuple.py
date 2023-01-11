'''
튜플
    튜플 몇 가지 점을 제외하곤 리스트와 거의 비슷하며 리스트와 다른 점은 다음과 같다.
    - 리스트 [] 으로, 튜플은 ()으로 초기화 한다.
    - 리스트 생성, 삭제, 수정이 가능, 튜플은 그 값을 변경 할 수 없다.
'''


def main():
    a = ('b', '1', 'o', 'g', 9, 8)
    # 튜플 값 전체 출력
    print('a:{}'.format(a))

    # 'tuple' object does not support item assignment
    # a[0] = 99

    # 'tuple' object doesn't support item deletion
    # del a[0]

main()
