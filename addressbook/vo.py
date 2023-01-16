'''
파일명 : vo.py
설 명 : Member
생성일 : 2023/01/16
생성자 : yanghanna
'''

class Member:
    # 생성자
    def __init__(self, id=None, name=None, passwd=None, email=None):
        self.id = id            # 아이디
        self.name = name        # 이름
        self.passwd = passwd    # 비번
        self.email = email      # 이메일

    # 인스턴스 변수들을 문자열로 변환
        def __str__(self):
            return 'id:{0}, name:{1}, pw:{2}, email:{3}'.format(self.id, self.name, self.passwd, self.email)

def main():
    a = Member('hanna', '한나', '1234', 'gkssk2309@naver.com')
    print(a)
    # vo.py 직접 실행 할 떄만 출력 : '__main__'으로 인식된다.

if __name__ == '__main__':
    main()
