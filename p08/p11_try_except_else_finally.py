'''

'''


def main():
    try:
        x = int(input('숫자를 입력하세요>'))
        y = 10 / x
    except ZeroDivisionError as e:
        print("숫자를 0으로 나눌 수 없습니다.", e)
    else:
        print("else:{}".format(y))  # 예외가 발생 하지 않았을 떄 수행
    finally:
        print('finally: 코드 수행이 종료 되었습니다.')



main()
