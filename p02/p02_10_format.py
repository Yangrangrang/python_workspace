'''

'''


def main():
    num = 5
    # I eat 3 apples.
    # 숫자 대입
    print('I eat %d apples.' % num) # I eat 5 apples.

    day = "five"
    # 문자 대입
    print('I eat %s apples' % day)  # I eat five apples

    # 인자 2개 대입
    # I eat 5 apples. so I was sick for five days.
    print("I eat %d apples. I was sick for %s days" % (num, day))

    # 10개의 문자열 공간을 확보하고 오른쪽 정렬: %10s
    print("1234567890")
    print("%10s" % ("hi"))
    print("-"*10)

    # 10개의 문자열 공간을 확보하고 왼쪽 정렬 : %-10s
    print("%-10s" % ("hi"))
    print("-" * 10)

    # 실수 출력 : 0.4 소수점 이하 4자리 까지 출력
    print("rate is %0.4f" % (1.414))




main()
