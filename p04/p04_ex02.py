'''
1부터 20까지의 정수 중에서 2 또는 3의 배수가 아닌 수의 총합을 구하시오.
'''


def main():
    a = list(range(1,21))
    print(a)
    number = 0

    for a in range(1,21):
        if a%2 != 0 and a%3 !=0:
            # print(a, end=',')
            number += a

    print(number)

    sum = 0 # 더하기
    for i in range(1,21):
        if i % 2 == 0 or i % 3 == 0: continue
        sum += i
        print(i, end=',')
    print('sum:{}'.format(sum))


main()
