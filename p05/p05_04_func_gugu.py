'''

'''

def gugu(dan):
    for i in range(1,10):
        print('{}*{}={}'.format(dan,i,(dan*i)))

def main():

    # 2단
    # 함수가 없는 형태
    for i in range(1,10):
        print('{}*{}={}'.format(2,i,(2*i)))

    print()

    # 함수가 있는 형태
    gugu(3)


main()
