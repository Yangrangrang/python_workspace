'''
파일명 : dao_mail.py
설 명 : MailDao
생성일 : 2023/01/17
생성자 : yanghanna
'''
import sqlite3

import pymysql

from cmn.common import WorkDiv
from mail.vo_mail import MailVo

class MailDao(WorkDiv):

    # 디비 연결을 위한 생성자
    def __init__(self):
        self.conn = None

    def connect(self):
        '''디비 연결'''
        try:
            # auto commit, isolation_level=None
            # self.conn = sqlite3.connect("/Users/yanghanna/Documents/BIG_AI0102/1. python/workspace/addressbook/addressbook.db",isolation_level=None)
            self.conn = pymysql.Connect(user='root', passwd='root', host='localhost', db='pymysql', charset='utf8')
        except Exception as e:
            print('-' * 35)
            print('connect:{}'.format(e))
            print('-' * 35)

    def disconn(self):
        '''디비 close'''
        try:
            self.conn.close()
        except Exception as e:
            print('-' * 35)
            print('disconn:{}'.format(e))
            print('-' * 35)

    def doSave(self,m:MailVo):
        flag = 0
        try:
            # 디비연결
            self.connect()
            print('param:{} {} {} {}'.format(m.id, m.title, m.contents, m.regDt))

            # cur
            cur = self.conn.cursor()
            print(cur)

            # sql
            sql = "INSERT INTO MAIL_CONTENT VALUES (%s,%s,%s,%s)"
            print(sql)
            cur.execute(sql, (m.id, m.title, m.contents, m.regDt))

            # commit
            self.conn.commit()

            # DB 수행 반영 건수
            flag = cur.rowcount
        except Exception as e:
            print('-' * 35)
            print('doSave:{}'.format(e))
            print('-' * 35)
        finally:
            self.disconn()
        return flag

    def doDelete(self, id:int):
        flag = 0
        try:
            self.connect()
            print('param.id:{}'.format(id))
            cur = self.conn.cursor()
            print('cur:{}'.format(cur))
            sql = "DELETE FROM MAIL_CONTENT WHERE id=%s"
            print('sql:{}'.format(sql))
            cur.execute(sql, (id, ))
            self.conn.commit()
            flag = cur.rowcount
        except Exception as e:
            print('-' * 35)
            print('doDelete:{}'.format(e))
            print('-' * 35)
        finally:
            self.disconn()
        return flag

    def doRetrieve(self,m:MailVo):
        outList = []
        try:
            # 1. 디비연결
            self.connect()

            # 2-1. cursor
            cur = self.conn.cursor()

            # 3. sql
            sql = '''SELECT id,name,passwd,email
                                FROM MAIL_CONTENT
                                WHERE id = %s '''

            # 4. sql 실행
            cur.execute(sql, (m.id, ))

            outList = [MailVo(id=row[0], title=row[1], contents=row[2], regDt=row[3]) for row in cur]

            for vo in outList:
                print(vo)

        except Exception as e:
            print('-' * 35)
            print('doRetrieve:{}'.format(e))
            print('-' * 35)
        finally:
            self.disconn()
        return outList

    def doUpdate(self):
        pass

    def doSelectOne(self, m:MailVo):
        outVO = None
        vo = None
        try:
            self.connect()
            print(m.id)
            cur = self.conn.cursor()
            print(cur)
            sql = "SELECT id,title,contents,reg_dt FROM MAIL_CONTENT WHERE id=%s"
            print(sql)
            cur.execute(sql, (m.id, ))

            outVO = [MailVo(id=row[0],title=row[1],contents=row[2],regDt=row[3]) for row in cur]

            if outVO != None and len(outVO)>0:
                vo = outVO[0]
                print('param:{} {} {} {} '.format(vo.id, vo.title, vo.contents, vo.regDt))

        except Exception as e:
            print('-' * 35)
            print('doSelectOne:{}'.format(e))
            print('-' * 35)
        finally:
            self.disconn()
        return vo
def addAndGet():
    a = MailDao()
    test = MailVo(id='1', title='test', contents='testcontents', regDt='a')
    a.doSave(test)


def main():
    if __name__ == '__main__':
        a = MailDao()
        test = MailVo(id='1', title='test', contents='testcontents', regDt='20240118')
        # flag = a.doSave(test)
        flag = a.doDelete(1)
        if flag == 1:
            print("성공")


main()
