'''

'''
def add_and_mul(a,b):
    return a+b, a*b

def main():
    result = add_and_mul(2,3)
    # result:(5, 6), type(result):<class 'tuple'>
    print('result:{}, type(result):{}'.format(result, type(result)))

    result01,result02 = add_and_mul(2,3)
    # result01:5
    # result02:6
    print('result01:{}'.format(result01))
    print('result02:{}'.format(result02))


main()
