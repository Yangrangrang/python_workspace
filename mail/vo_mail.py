'''
파일명 : vo_mail.py
설 명 : 
생성일 : 2023/01/17
생성자 : yanghanna
'''

class MailVo:
    '''메일 내용 관리'''

    def __init__(self, id=None, title=None, contents=None, regDt=None):
        self.id = id
        self.title = title
        self.contents = contents
        self.regDt = regDt

    # 인스턴스 변수들을 문자열로 변환
    def __str__(self):
        return 'id:{}, title:{}, contents:{}, regDt:{}'.format(self.id, self.title, self.contents, self.regDt)


def main():
    a = MailVo(1, 'test', 'testcontents', 'gkssk2309@naver.com')
    print(a)

if __name__ == '__main__':
    main()
