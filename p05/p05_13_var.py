'''

'''

# 함수 안에서 함수 밖의 변수를 변경할 수 있다.(global)
a = 1

def func01():
    global a
    a = a+1

def main():
    func01()
    print('a:{}'.format(a))


main()
