'''

'''


def main():
    try:
        x = int(input("숫자를 입력하세요>"))
        y = 10 / x
        print('1 ',y)
    except ZeroDivisionError:
        print('숫자를 0으로 나눌 수 없습니다.')


main()
