'''
문자열 제거 함수
    strip(제거할 값) : 양쪽 끝에서 특정 값을 제거
    lstrip(제거할 값) : 왼쪽 끝에서 특정 값을 제거
    rstrip(제거할 값) : 왼쪽 끝에서 특정 값을 제거
'''


def main():
    a = '  abc  '
    print('a:{}'.format(a))
    print(a.strip())
    print(a.lstrip())
    print(a.rstrip())

    a = "***abc***"
    print("a:{}".format(a))
    print(a.strip("*"))
    print(a.lstrip("*"))
    print(a.rstrip("*"))



main()
