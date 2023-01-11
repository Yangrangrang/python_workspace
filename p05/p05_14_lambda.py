'''

'''
def add(a,b):
    return a + b

def main():
    result = add(11,13)
    print('result:{}'.format(result))

    print('11+13의 합',(lambda a,b:a+b)(11,13))


main()
