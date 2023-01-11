'''
총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격, 그렇지 않으면 불합격
    kor = [90,25,67,45,80]
    continue 건너뛰기
'''


def main():
    kor = [90, 25, 67, 45, 80]
    number = 0

    for i in kor:
        number += 1

        if i < 60: continue
        print("{}번 학생은 합격".format(number))



main()
