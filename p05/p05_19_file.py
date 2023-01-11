'''

'''


def main():
    # 파일 패스 구분자는: /
    f= open("/Users/yanghanna/Documents/BIG_AI0102/1. python/pcmk01.txt",'w')

    for i in range(1,11):   # 1-(11-1)
        data = "%d 오늘은 매우 즐거운 금요일입니다.\n"% i
        f.write(data)

    f.close()
main()
