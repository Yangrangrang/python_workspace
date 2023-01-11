'''

'''


def main():
    try:
        x = int(input('나눌숫자를 입력하세요>'))
        y = 10 / x
        print("1 ",y)
    except: # 예외 발생 시 실행
        print('예외가 발생 했습니다.')

    print("2 완료")

main()
