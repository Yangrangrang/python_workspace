'''
파일 내용 읽기
'''


def main():
    f = open("/Users/yanghanna/Documents/BIG_AI0102/1. python/pcmk01.txt",'r')
    # 한줄만 읽는다. : 데이터 편집이 필요한 경우 사용
    # line = f.readline()

    while True:
        line = f.readline()
        if not line : break
        print(line.rstrip("\n"))    # 개행 문자 제거

    print(line)


main()
