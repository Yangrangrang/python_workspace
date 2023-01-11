'''

'''


def main():
    c = [100,200,300,400,500,600,700]
    print("*"*40)
    print("c:{}".format(c))
    print("*" * 40)

    # 특정위치
    del(c[1])
    print("c:{}".format(c)) # c:[100, 300, 400, 500, 600, 700]

    # 범위 삭제
    del(c[1:4])
    print('c:{}'.format(c)) # c:[100, 600, 700]



main()
