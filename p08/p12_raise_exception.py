'''

'''


def main():
    try:
        x = int(input('3의 배수를 입력하세요>'))

        if x % 3 != 0:                          # 3의 배수가 아니면
            raise Exception('3의 배수가 아닙니다.')  # 예외를 발생 시킴
        print(x)
    except Exception as e:
        print("예외발생", e)


main()
