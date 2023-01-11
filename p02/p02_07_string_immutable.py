'''

'''


def main():
    str = "Hello World"
    print("str:{}".format(str))
    # str[0] = 'h'  #ERR : 이렇게 0번째 문자를 바꿀수 없다.

    str = 'h' + str[1:]
    print("str:{}".format(str))

main()
'''
str:Hello World
str:hello World
'''
