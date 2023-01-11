'''
1+(-2)+3+(-4)+....식으로 더해 나갔을때, 몇가지 더해야 총합이 100이상 되는지 구하시오.
'''


def main():
    num = 0
    cnt = 0
    while num <= 100:
        for i in range(1000):
            if i%2 == 0:
                i = -i
            # print(i, end=',')
            num += i
            # print(num,end=',')
            # cnt += 1

    sum = 0 # 총합 저장 변수
    i = 1   # 증가값
    num = 0
    sign = 1    # 부호변수

    while True:
        # 음수 / 양수
        if i % 2 == 0: sign = -1
        else: sign = 1
        num = i * sign
        sum = sum + num
        i = i + 1

        print(num,end=" ")


        if sum >= 100:
            break

    print('sum:{}'.format(sum))
    print('num:{}'.format(num))


main()
