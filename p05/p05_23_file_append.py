'''

'''


def main():
    # 기존 파일에 추가 (a)
    f = open("/Users/yanghanna/Documents/BIG_AI0102/1. python/pcmk01.txt", 'a',encoding='UTF-8')
    for i in range(11,21):
        data = '%d 오늘은 매우 즐거운 금요일입니다.\n' % i
        f.write(data)

    f.close()

    print('파일에 내용 추가 완료')


main()
