'''

'''

def func01(*args):
    result = 0
    for i in args:
        result += i

    return result

def main():
    a = func01(1,2)
    print('a:{}'.format(a))

    b = func01(1,2,3,4,5,6,7,8,9,10)
    print('b:{}'.format(b))

    # param 개수가 0개 인 경우
    c = func01()
    print('c:{}'.format(c))     # c:0

main()
