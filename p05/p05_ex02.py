'''
사용자의 입력을 (test.txt)에 저장하는 프로그램을 작성해 보자
( 단 프로그램을 다시 실행하더라도 기존에 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)
'''
import sys

def main():

    # with open("/Users/yanghanna/Documents/BIG_AI0102/1. python/test.txt", 'a') as f:
    #     str = input('입력하세요>')
    #     f.write(str + '\n')
    # print("파일 생성이 완료 되었습니다.")

    user_input = input('저장할 내용을 입력하세요.')
    f = open('test01.txt','a')  # 내용 추가 입력
    f.write(user_input) # 내용 기록
    f.write("\n")
    f.close()   # 파일 자원 반납

    print('파일 생성이 완료 되었습니다. 입력내용 :{}'.format(user_input))



main()
