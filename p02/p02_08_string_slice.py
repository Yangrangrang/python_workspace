'''
Life is too short, You need Python
'''


def main():
    str01 = "Life is too short, You need Python"
    print("-"*35)
    print(str01)
    print("12345678901234567890123456789012345")
    print("-"*35)

    # Life str01[0:4]
    # 0<=str01<4
    print("str01[0:4]:{}".format(str01[0:4]))

    # str01[0:5] : 공백문자 포함
    # str01[시작번호:끝번호]
    print("str01[0:5]:{}".format(str01[0:5]))

    # str01[시작번호:끝번호] 시작번호:끝번호 모두 생략    # str01[:]:Life is too short, You need Python
    print('str01[:]:{}'.format(str01[:]))

    # str01[시작번호:끝번호] 시작번호 생략 (0번째 부터 시작)   # str01[:17]:Life is too short
    print('str01[:17]:{}'.format(str01[:17]))

    # str01[시작번호:끝번호] 끝번호 생략 (시작번호부터 끝까지)   # str01[19:]:You need Python
    print('str01[19:]:{}'.format(str01[19:]))

    # str01[시작번호:끝번호] 시작은 양수, 끝은 음수
    print("str01[19:-7]:{}".format(str01[19:-7]))   # str01[19:-7]:You need
main()
