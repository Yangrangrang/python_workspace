'''

'''

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

# mod1.py를 직접 실행 할 때만 출력 : __main__으로 인식 된다.
if __name__ == '__main__':
    print('__name__:{}'.format(__name__))
    print(add(1,11))
    print(sub(1,11))
