'''

'''


def main():
    # 파일 생성
    # with open('test02.txt','w') as f:
    #     f.write("Life is too short \n you need java.")

    # 내가 쓰다 만 코드....
    # f = open('test02.txt', 'r')
    # lines = f.read()
    # print(lines)
    # find_str = 'java'
    # print(lines.find('java'))
    # idx = lines.find('java')
    # if idx != -1:
    #     pass
    # f.close()

    # 강사님 코드
    #1. test02.txt읽는다.
    #2. java to python
    #3. test02.txt 변경된 내용을 기록한다.

    1.
    f = open('test02.txt','r')
    body = f.read()
    print("body:{}, type(body):{}".format(body,type(body)))
    f.close()

    # 2.
    body = body.replace('java', 'python')
    print('after body:{}'.format(body))

    # # 3.
    # f = open('test02.txt','w')
    # f.write(body)
    # f.close()

    with open('test02.txt','w') as f:
        f.write(body)

    print('수정완료')





main()
