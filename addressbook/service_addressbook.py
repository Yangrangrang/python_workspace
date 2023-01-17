'''
파일명 : service_addressbook.py
설 명 : addressbook service
생성일 : 2023/01/17
생성자 : yanghanna
'''

from vo import Member
from dao_addressbook import AddressbookDao

class AddressbookService:
    def __init__(self):
        self.dao = None

    def doSelectOne(self,member:Member):
        '''단건 조회'''
        self.dao = AddressbookDao() # dao 객체 생성
        # ID 입력
        print('doSelectOne.id:{}'.format(member.id))
        outVo = self.dao.doSelectOne(m=member)
        return outVo

    def doDelete(self,member:Member):
        '''단건 삭제'''
        self.dao = AddressbookDao()
        return self.dao.doDelete(member.id)

    def doSave(self,member:Member):
        '''등록'''
        self.dao = AddressbookDao()
        return self.dao.doSave(member)

    def doUpdate(self,member:Member):
        '''수정'''
        self.dao = AddressbookDao()
        return self.dao.doUpdate(member)

    def doRetrieve(self,searchDiv,searchWord):
        '''목록 조회'''
        self.dao = AddressbookDao()
        return self.dao.doRetrieve(searchDiv,searchWord)

def main():
    if __name__ == '__main__':
        a = AddressbookService()
        outVo = a.doSelectOne()
        print('outVo:{}{}{}{}'.format(outVo.id, outVo.name, outVo.passwd, outVo.email))


main()
