'''

'''
a = 1   # 전역변수

def func02(a):
    a = a+1 # 지역변수
    return a

def main():
    # print(func02(a))
    a = func02(1)

    print(a)

main()
