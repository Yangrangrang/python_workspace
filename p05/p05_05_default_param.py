'''

'''

def func01(a, b=11, c=13):
    return a + b + c

def func02(a=10, b=20):
    return a + b

def main():

    print('func02(1,2):{}'.format(func02(1,2)))
    func02(1)
    func02()

    print('func01(1,2,3):{}'.format(func01(1,2,3))) # func01(1,2,3):6
    print('func01(1,2):{}'.format(func01(1, 2)))    # func01(1,2):16
    print('func01(1):{}'.format(func01(1)))         # func01(1):25
    # print('func01():{}'.format(func01()))           # TypeError: func01() missing 1 required positional argument: 'a'

main()
