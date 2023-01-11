'''

'''


def main():
    # console param 입력
    num = int(input("숫자를 입력하세요>"))

    # num:2, type(num):<class 'str'>
    print('num:{}, type(num):{}'.format(num, type(num)))

    if 0 == num :
        print("입력한 숫자는 {0} 입니다.".format(num))

    print("무조건 수행!")


main()
