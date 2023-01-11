'''
문자열.find(찾을 값, 시작인덱스, 종료인덱스) : 문자열 시작~종료 인덱스 사이에 찾을 값이 처음 나타나는 위치를 반환
문자열.index(찾을 값, 시작인덱스, 종료인덱스) : 문자열 시작~종료 인텍스 사이에 찾을 값이 처음 나타나는 위치를 반환
    find와 index의 차이는 값이 없는 경우 find -1을 출력, index는 AttributeError 발생
문자열.rfind(찾을 값) : 문자열 끝나는 위치부터 시작하여 찾을 문자열이 처음 나타나는 위치
'''


def main():
    # find
    a = 'abcdefabcdef'
    print(a.find('c'))  # 2
    print(a.find('cde'))    # 2 첫번째 인덱스
    print(a.find('c', 0, 5))    # 2
    print(a.find('z'))  # 찾는 문자가 없는 경우 -1

    # index
    print(a.index('c'))  # 2
    # print(a.index('z'))  # ValueError: substring not found

    a = "p02._func.txt" # 파일 확장자 찾기
    # rfind
    print(a.rfind('.'))
    i = a.rfind('.')
    print(a[i+1:])  # txt : i + 1 '.'을 제외한 확장자만 추출
main()
