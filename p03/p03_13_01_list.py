'''
    리스트 생성
'''


def main():
    a = ["python", 333]
    print('a:{}'.format(a))     # a:['python', 333]

    b = [1, 2, 3]
    print("b:{}".format(b))

    # 리스트 덧셈
    print("a+b:{}".format(a + b))   # a+b:['python', 333, 1, 2, 3]

    # 리스트 곱셈
    c = b * 3
    print("b*3:{}".format(c))   # b*3:[1, 2, 3, 1, 2, 3, 1, 2, 3]
    d = b * 0
    print("b*0:{}".format(d))   # b*0:[] list 초기화

    # f0 = a * b
    # print('f0:{}'.format(f0))

    g = [1, 2, 3]
    # can't multiply sequence by non-int of type 'list'
    # print('g0:{}'.format(b*g))

main()
