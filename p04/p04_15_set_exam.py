'''

'''


def main():
    # 집합 중복 제거
    s1 = {1,1,2,2,3,3,'a','a','mask','mask','b'}
    # s1:{1, 2, 3, 'a', 'b', 'mask'},type(s1):<class 'set'>
    print('s1:{},type(s1):{}'.format(s1, type(s1)))

    # list -> set(중복제거) -> list
    result01 = [1,1,1,1,1,'a','a','list','list',1,1,1]
    print('result01:{}, type(result01):{}'.format(result01, type(result01)))
    # result01:[1, 1, 1, 1, 1, 'a', 'a', 'list', 'list', 1, 1, 1], type(result01):<class 'list'>

    s2 = set(result01)
    print('s2:{}'.format(s2))
    # s2:{1, 'a', 'list'}

    list01 = list(s2)
    print('list01:{}'.format(list01))
    # list:['list', 1, 'a']

    result01 = (1, 1, 1, 1, 1, 'a', 'a', 'list', 'list', 1, 1, 1)
    print('result01:{}, type(result01):{}'.format(result01, type(result01)))
    s3 = set(result01)
    print('list(s3):{}'.format(tuple(s3)))

main()
