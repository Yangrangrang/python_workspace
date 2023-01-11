'''
숫자형 : 정수, 실수

'''
def main():
    # 정수
    num = 123
    # num : 123, type<class 'int'>
    print("num : {0}, type{1}".format(num,type(num)))

    # 실수
    fNum = 1.2
    # fNum : 1.2,type<class 'float'>
    print("fNum : {},type{}".format(fNum,type(fNum)))

    fNum = 4.12E10 # 4.12 * 10에 10승 (10 ** 10)
    # fNum: 41200000000.0,type<class 'float'>
    print("fNum: {},type{}".format(fNum,type(fNum)))

    fNum = 4.12E-10  # 4.12 * 10에 10승 (10 ** 10)
    # fNum: 4.12e-10,type<class 'float'>
    print("fNum: {},type{}".format(fNum, type(fNum)))
main()