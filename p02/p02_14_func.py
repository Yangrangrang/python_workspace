'''
replace, upper, lower
    문자열.replace(기존값, 변경할 값, 변경횟수)
    문자열.upper() : 알파벳 소문자를 대문자로 변환
    문자열.lower() : 알파벳 대문자를 소문자로 변환
'''


def main():
    a = 'a,b,c,d,e'
    print(a.replace("," , "/"))     # a/b/c/d/e (횟수를 생략하면 전체)
    print(a.replace(",", "/", 1))   # a/b,c,d,e

    a = 'a,b,c,D,E'
    print(a.upper())    # A,B,C,D,E
    print(a.lower())    # a,b,c,d,e


main()
