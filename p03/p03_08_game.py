'''

'''
import random

def main():
    # range(1, 11) 1 <= i < 11 증가 1씩
    # for i in range(1,11):
    #     com = random.randint(1, 3)
    #     print('i:{}, com:{}'.format(i, com))

    com = random.randint(1, 3)
    user = int(input('가위(1), 바위(2), 보(3) 선택>'))
    print('com:{}'.format(com))
    print('user:{}'.format(user))

    sum = com - user

    # if sum == -1 or sum == 2:
    #     print("사용자 승")
    # elif sum == 1 or sum == -2:
    #     print("컴퓨터 승")
    # elif sum == 0:
    #     print("무승부")

    # in 으로 전환
    if sum in [2, -1]:
        print("사용자 승")
    elif sum in [1, -2]:
        print("컴퓨터 승")
    elif sum in [0]:
        print("무승부")


main()
