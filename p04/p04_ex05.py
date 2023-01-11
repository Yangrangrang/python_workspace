'''
두 개의 주사위를 던졌을 때 눈의 합이 6이 되는 모든 경우의 수를 출력하는 프로그램을 작성하시오.
'''


def main():
    cnt = 0
    for i in range(1,7):
        # print(i, end=",")
        for j in range(1,7):
            if i + j == 6:
                cnt += 1
                print('{}+{}={}'.format(i,j,i+j))
    print(cnt)


main()
