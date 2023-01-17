'''
파일명 : view_menu.py
설 명 : 
생성일 : 2023/01/17
생성자 : yanghanna
'''
from service_addressbook import AddressbookService
from vo import Member

class Menu:
    ''' 저장(1), 삭제(2), 단건조회(3), 수정(4), 목록조회(5), 메일전송(10), 종료(7) '''

    def __init__(self):
        self.service = None

    def run(self):
        '''Menu 보여주고, 입력 받기'''
        '''1. 무한루프
           2. menu를 입력받는다.
           3. 입력받은 메뉴를 수행한다.
           ...
           5. 7번이 들어오면 좋료한다.'''

        while True:
            menu = int(input('저장(1), 삭제(2), 단건조회(3), 수정(4), 목록조회(5), 메일전송(10), 종료(7)>'))
            self.service = AddressbookService()
            member = Member()

            if menu == 1:
                member.id = input('아이디를 입력하세요>')
                member.name = input('이름을 입력하세요>')
                member.passwd = input('비번을 입력하세요>')
                member.email = input('이메일을 입력하세요>')
                flag = self.service.doSave(member)
                if flag == 1:
                    print(member.id + '가 등록 되었습니다.')
                else:
                    print(member.id + '등록 실패!')

            if menu == 2:
                member.id = input('삭제할 ID를 입력하세요>')
                flag = self.service.doDelete(member)
                if flag == 1:
                    print(member.id + '가 삭제되었습니다.')
                else:
                    print(member.id + '삭제 실패!')

            if menu == 3:
                member.id = input('조회 ID를 입력하세요>')
                outMember = self.service.doSelectOne(member)
                if outMember != None:
                    print('outMember:{}{}{}{}'.format(outMember.id, outMember.name, outMember.passwd, outMember.email))
                else:
                    print('아이디를 확인하세요')

            if menu == 4:
                member.id = input('수정할 아이디를 입력하세요>')
                member.name = input('수정할 이름을 입력하세요>')
                member.passwd = input('수정할 비번을 입력하세요>')
                member.email = input('수정할 이메일을 입력하세요>')
                flag = self.service.doUpdate(member)
                if flag == 1:
                    print(member.id + '가 수정 되었습니다.')
                else:
                    print(member.id + '수정 실패!')

            if menu == 5:
                searchDiv = input('검색 구분을 입력하세요\n (전체:"", 아이디:10, 이름:20, 이메일:30) >')
                searchWord = input('검색어를 입력하세요 >')
                outList = self.service.doRetrieve(searchDiv,searchWord)
                for vo in outList:
                    print('member:{}, {}, {}, {}'.format(vo.id, vo.name, vo.passwd, vo.email))

            if menu == 7:
                print('프로그램을 종료 합니다.')
                break





def main():
    m = Menu()
    m.run()


main()
