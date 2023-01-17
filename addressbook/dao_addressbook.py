'''
파일명 : dao_addressbook.py
설 명 : AddressbookDao
생성일 : 2023/01/16
생성자 : yanghanna
'''
import sqlite3
from cmn.common import WorkDiv  #cmn 패키지. common모듈 에 WorkDiv
from vo import Member

class AddressbookDao(WorkDiv):
    def __init__(self):
        self.conn = None    # DB Connection 연결

    def getCount(self):
        '''전체 건수'''
        count = 0
        try:
            self.connect()
            cur = self.conn.cursor()
            sql = "SELECT count(*) cnt FROM addressbook"
            print('sql:{}'.format(sql))
            cur.execute(sql)

            # 데이터 조회
            count = [row[0] for row in cur]
            print('count:{}'.format(count))

        except Exception as e:
            print('-' * 35)
            print('getCount:{}'.format(e))
            print('-' * 35)
        finally:
            self.disconn()
        return count[0]


    def disconn(self):
        '''DB 자원 반납'''
        try:
            self.conn.close();
        except Exception as e:
            print('-' * 35)
            print('disconn:{}'.format(e))
            print('-' * 35)
    def connect(self):
        '''DB 연결'''
        try:
            self.conn = sqlite3.connect("/Users/yanghanna/Documents/BIG_AI0102/1. python/workspace/addressbook/addressbook.db")
        except Exception as e:
            print('-'*35)
            print('connect:{}'.format(e))
            print('-'*35)

    def doSave(self, m:Member):
        flag = 0
        try:
            #1. DB 연결
            self.connect()

            #2. param 확인
            print('param:{}'.format(m))

            #2-1. cursor 객체 생성
            cur = self.conn.cursor()
            print('cur:{}'.format(cur))

            #3. sql 정의
            sql = "INSERT INTO ADDRESSBOOK VALUES (?,?,?,?)"
            print('sql:{}'.format(sql))

            #4. sql 실행
            cur.execute(sql, (m.id, m.name, m.passwd, m.email))

            #5. 트랜젝션 처리
            self.conn.commit()
            flag = cur.rowcount

        except Exception as e:
            print('-' * 35)
            print('doSave:{}'.format(e))
            print('-' * 35)
        finally:
            self.disconn()

        return flag

    def doUpdate(self, m:Member):
        flag = 0
        try:
            self.connect()
            print('param:{}'.format(m.id, m.passwd, m.name, m.email))

            cur = self.conn.cursor()
            sql = "UPDATE ADDRESSBOOK SET NAME=?, PASSWD=?, EMAIL=? WHERE id=?"

            cur.execute(sql, (m.name, m.passwd, m.email, m.id))
            self.conn.commit()
            flag = cur.rowcount
        except Exception as e:
            print('-' * 35)
            print('doUpdate:{}'.format(e))
            print('-' * 35)
        finally:
            self.disconn()
        return flag

    def doDelete(self, id:int):
        flag = 0
        try:
            self.connect()
            print('param:{}'.format(id))

            cur = self.conn.cursor()
            print('cur:{}'.format(cur))

            sql = "DELETE FROM ADDRESSBOOK WHERE id=?"
            print('sql:{}'.format(sql))

            cur.execute(sql, (id,))

            self.conn.commit()
            flag = cur.rowcount # 반영된 건수
            print('doDelete().cur.rowcount:{}'.format(cur.rowcount))
        except Exception as e:
            print('-' * 35)
            print('doDelete:{}'.format(e))
            print('-' * 35)
        finally:
            self.disconn()
        return flag

    def doSelectOne(self, m:Member):
        outVO = None
        vo = None
        try:
            self.connect()
            print('member:{}'.format(m.id))

            cur = self.conn.cursor()

            sql = "SELECT id,name,passwd,email FROM ADDRESSBOOK WHERE id=?"
            print('sql:{}'.format(sql))

            cur.execute(sql, (m.id,))

            # 데이터 조회 : 리스트 내포
            outVO = [Member(id=row[0], name=row[1], passwd=row[2], email=row[3]) for row in cur ]
            if outVO != None and len(outVO)>0:
                vo = outVO[0]
                print('outVO:{} {} {} {}'.format(vo.id, vo.name, vo.passwd, vo.email))

        except Exception as e:
            print('-' * 35)
            print('doSelectOne:{}'.format(e))
            print('-' * 35)
        finally:
            self.disconn()
        return vo

    def doRetrieve(self, searchDiv='', searchWord=''):
        '''목록조회: 검색구분(아이디:10 이름:20 이메일:30, 검색어'''
        outList= []
        try:
            # 1. 디비연결
            self.connect()

            # 2.param 확인
            print('searchDiv:{}, searchWord:{}'.format(searchDiv,searchWord))

            # 2-1. cursor
            cur = self.conn.cursor()

            # 3. sql
            sql = '''SELECT id,name,passwd,email
                        FROM ADDRESSBOOK
                        WHERE 1=1 '''

            sqlWhere = ""

            if searchDiv == "10":
                sqlWhere = "AND id like ?"  # mysql  ? -> %s 사용
            elif searchDiv == "20":
                sqlWhere = "AND name like ?"
            elif searchDiv == "30":
                sqlWhere = "AND email like ?"

            # 동적 sql
            sql = sql + "\n" + sqlWhere
            print('sql:{}'.format(sql))

            # 4. sql 실행

            if searchDiv != "":
                cur.execute(sql, (searchWord+'%',))
            else:
                cur.execute(sql, )

            outList = [Member(id=row[0],name=row[1],passwd=row[2],email=row[3]) for row in cur]

            for vo in outList:
                print(vo)

        except Exception as e:
            print('-' * 35)
            print('doRetrieve:{}'.format(e))
            print('-' * 35)
        finally:
            self.disconn()
        return outList

def doRetrieveTest():
    a = AddressbookDao()
    # 아이디:10 이름:20 이메일:30
    searchDiv = "20"
    searchWord = "한나"
    mList = a.doRetrieve(searchDiv,searchWord)
    print(mList)

def addAndGet():
    #1. 데이터 삭제
    #2. 등록
    #3. 조회
    #4. 비교

    a = AddressbookDao()  # AddressbookDao 생성
    m01 = Member(id=1, name='한나', passwd='1234', email='gkssk2309@naver.com')
    m02 = Member(id=2, name='한나1', passwd='1234', email='gkssk1@naver.com')
    m03 = Member(id=3, name='한나2', passwd='1234', email='gkssk2@naver.com')

    a.doDelete(m01.id) # 삭제
    a.doDelete(m02.id)  # 삭제
    a.doDelete(m03.id)  # 삭제

    flag = a.doSave(m01)    # 등록
    count = a.getCount()
    if count == 1:
        print('1등록 성공')
    else:
        print('1등록 실패')

    flag = a.doSave(m02)
    if a.getCount() == 2:
        print('2등록 성공')
    else:
        print('2등록 실패')


    flag = a.doSave(m03)
    if a.getCount() == 3:
        print('3등록 성공')
    else:
        print('3등록 실패')

    out01 = a.doSelectOne(m01)  # 비교
    out02 = a.doSelectOne(m02)
    out03 = a.doSelectOne(m03)

    if  isSameData(m01,out01) == 1:
        print('1addAndGet 성공')
    else:
        print('1addAndGet 실패')

    if  isSameData(m02,out02) == 1:
        print('2addAndGet 성공')
    else:
        print('2addAndGet 실패')

    if  isSameData(m03,out03) == 1:
        print('3addAndGet 성공')
    else:
        print('3addAndGet 실패')

def isSameData(org:Member,vsVO:Member):
    '''입력, 조회데이터 비교'''
    if org.id != vsVO.id:
        return 0

    if org.name != vsVO.name:
        return 0

    if org.passwd != vsVO.passwd:
        return 0

    if org.email != vsVO.email:
        return 0

    return 1

def update():
    a = AddressbookDao()
    m01 = Member(id=1, name='한나', passwd='1234', email='gkssk2309@naver.com')
    m02 = Member(id=2, name='한나1', passwd='4321', email='gkssk1@naver.com')
    m03 = Member(id=3, name='한나2', passwd='1234', email='gkssk2@naver.com')

    # 1. 기존 데이터 삭제
    a.doDelete(m01.id)
    a.doDelete(m02.id)
    a.doDelete(m03.id)

    # 2. 데이터 등록
    a.doSave(m01)
    if a.getCount() == 1:
        print("1성공")
    else:
        print("1실패")

    # 3. 데이터 조회
    out01 = a.doSelectOne(m01)
    if isSameData(m01, out01) == 1:
        print("1조회 성공")
    else:
        print("1조회 실패")

    # 4. 조회 데이터 수정
    # m01 = Member(id=1, name='한나1', passwd='4321', email='gkssk1@naver.com')
    upData = '-U'
    out01.id = out01.id
    out01.name = out01.name + "" + upData
    out01.passwd = out01.passwd + "" + upData
    out01.email = out01.email + "" + upData


    # 5. update
    # flag = a.doUpdate(m01)
    flag = a.doUpdate(out01)
    if flag == 1:
        print("2성공")
    else:
        print("2실패")

    # 6. 조회(업데이트된 데이터)
    # v01 = a.doSelectOne(m01)
    upOut01 = a.doSelectOne(out01)

    # 7. 비교
    # a = isSameData(m01, v01)
    a = isSameData(out01, upOut01)
    if a == 1:
        print("3성공")
    else:
        print("3실패")

def main():
    # a = AddressbookDao()    # AddressbookDao 생성
    # a.connect() #DB 연결
    # addAndGet()
    # update()

    # m01 = Member(id=1, name='한나', passwd='1234', email='gkssk2309@naver.com')
    # m02 = Member(id=2, name='한나1', passwd='1234', email='gkssk1@naver.com')
    # m03 = Member(id=3, name='한나2', passwd='1234', email='gkssk2@naver.com')


    # flag = a.doSave(m01)
    # if flag == 1:
    #     print('단건 등록 성공:{}'.format(1))

    # flag = a.doDelete(m01.id)
    # if flag == 1:
    #     print('단건 삭제 성공:{}'.format(1))

    # 단건 조회
    # vo = a.doSelectOne(m01)
    # if vo != None:
    #     print("단건조회 성공:{}".format(vo))

    # 수정
    # vo.name = '한나01'
    # vo.passwd = '4321'
    # vo.email = 'gkssk2309@naver.com'
    # # m02 = Member(id=1, name='양한나', passwd='1234', email='gkssk2309@gmail.com')
    # flag = a.doUpdate(vo)
    # if flag == 1:
    #     print("수정 성공:{}".format(flag))

    #------------------------------------------
    if __name__ == '__main__':
        addAndGet()
        doRetrieveTest()

main()
