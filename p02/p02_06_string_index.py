'''
H   e   l   l   o
0   1   2   3   4
-5  -4  -3  -2  -1
'''


def main():
    str01 = "Hello"
    print("--"*10)
    print("str01:{}".format(str01))
    print("str01:01234")
    print("--"*10)

    print('str01[1]:{}'.format(str01[1]))
    print('str01[-1]:{}'.format(str01[-1]))
    print("str01의 문자열 길이:{}".format(len(str01)))
main()
'''
--------------------
str01:Hello
str01:01234
--------------------
str01[1]:e
str01[-1]:o
str01의 문자열 길이:5
'''
