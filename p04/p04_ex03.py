'''
1+(1+2)+(1+2+3)+(1+2+3+4)+...+(1+2+...+10)의 결과를 계산하시오.
'''


def main():
    sum = 0
    totalSum = 0
    for a in range(10):
        # print(a+1)
        sum += a+1
        totalSum += sum
        print('sum:{}'.format(sum))
    print(totalSum)

    sum = 0
    totalSum = 0

    for num in range(1,11):
        sum += num
        totalSum += sum
        print('totalSum:{}'.format(totalSum), end=", ")

    print(totalSum)

main()
