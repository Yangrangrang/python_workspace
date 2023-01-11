'''
두 변수에 값 교환
'''

def main():
    x = 12
    y = 14

    print("값 교환 전 x:{}, y:{}".format(x, y))

    # 교환
    tmp = x
    x = y
    y = tmp
    print("값 교환 후 x:{}, y:{}".format(x, y))

main()