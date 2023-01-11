'''
split(구분자) : 문자열을 구분자 기준으로 나눔
join(문자열 or 리스트) : 문자열 사이에 구분자를 추가
'''


def main():
    str = 'ab,c d,e fgh'
    # ['ab,c', 'd,e', 'fgh']
    print(str.split())  # 공백 기준 자르기 list return

    # ['ab', 'c d', 'e fgh']
    print(str.split(','))   # 쉼표 기준 자르기

    str = 'ab cde'
    print('/'.join(str))    # a/b/ /c/d/e
    print(','.join(str))    # a,b, ,c,d,e


main()
