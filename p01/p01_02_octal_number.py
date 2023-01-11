'''
8진수(octal) : 0o(숫자 0 + 알파벳 o or O)로 시작하면 된다.
16진수(Hexadecimal) : 0x (숫자 0 + 알파벳 x or X)로 시작하면 된다.

'''
def main():
    num = 0o177

    # 127의 자료형은 <class 'int'>
    print("{0}의 자료형은 {1}".format(num, type(num)))

    num = 0xB
    # 11의 자료형은 <class 'int'>
    print('{}의 자료형은 {}'.format(num, type(num)))
main()