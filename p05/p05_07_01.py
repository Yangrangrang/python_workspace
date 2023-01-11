'''

'''
def calc(sel, *args):
    if sel == 'add':
        result = 0
        for i in args:
            result += i
        return result
    elif sel == 'mul':
        result = 1
        for i in args:
            result *= i
        return result

def main():
    result = calc('add', 1,10,100,1000)
    print('result:{}'.format(result))

    result = calc('mul', 1,10,100)
    print('result:{}'.format(result))



main()
