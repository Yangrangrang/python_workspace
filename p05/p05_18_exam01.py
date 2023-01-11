'''

'''
import random


def lotto():
    # 리스트 내포 : 1~46
    ball = [x for x in range(1,47)]

    for i in range(0,10):
        # 0~45 사이 난수 발생
        idx = random.randint(0,45)

        tmp = ball[i]
        ball[i] = ball[idx]
        ball[idx] = tmp

    return ball
def ball_sort(result):
    # bubble sort
    for i in range(len(result)):
        for j in range(len(result)-i-1):
            # 오름차순
            if (result[j] > result[j+1]):
                result[j], result[j+1] = result[j+1], result[j]
                # temp = resuly[j]
                # result[j] = result[j+1]
                # result[j+1] = temp
    return result

def main():
    ball = lotto()
    ball_six = ball[0:6]
    result = ball_six
    print('result:{}'.format(result))
    result.sort(reverse=True)   #DESC 정렬
    print('desc result:{}'.format(result))
    print('result:{}'.format(ball_sort(result)))

    # a = ()
    # d = len(a)
    # print(a,type(a))
    # print(d)
    # b = {}
    # print(b,type(b))
    # c = []
    # print(c,type(c))

main()


