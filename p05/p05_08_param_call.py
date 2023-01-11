'''

'''

def add (a,b):
    return a + b

def main():
    # result=24
    result = add(a = 11, b= 13)
    print('result={}'.format(result))

    # 파라미터 이름을 지정해서 순서에 상관없이 호출
    result = add(b=16,a=13)
    print('result={}'.format(result))


main()
