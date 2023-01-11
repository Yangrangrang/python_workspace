'''

'''

def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요>'))
        if x % 3 != 0:
            raise Exception('3의 배수가 아닙니다.') # 예외 발생
        print(x)
    except Exception as e:
        print('three_multiple():{}'.format(e))
        raise e

def main():
    try:
        three_multiple()
    except Exception as e:
        print("예외 발생>>", e)

main()
