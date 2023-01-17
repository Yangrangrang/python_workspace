'''
파일명 : dao_mail.py
설 명 : MailDao
생성일 : 2023/01/17
생성자 : yanghanna
'''
import sqlite3
from cmn.common import WorkDiv
from vo_mail import MailVo

class MailDao(WorkDiv):

    # 디비 연결을 위한 생성자
    def __init__(self):
        self.conn = None

    def connect(self):
        '''디비 연결'''
        try:
            self.conn = sqlite3.connect("/Users/yanghanna/Documents/BIG_AI0102/1. python/workspace/addressbook/addressbook.db")
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
            print('param:{}'.format(m))

            # cur
            cur = self.conn.cursor()
            print(cur)

            # sql
            sql = "INSERT INTO MAIL_CONTENT VALUES (?,?,?,?)"
            print(sql)
            cur.execute(sql, (m.id, m.title, m.contents, m.regDt))

            # commit
            self.conn.commit()
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
            sql = "DELETE FROM MAIL_CONTENT WHERE id=?"
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

    def doRetrieve(self):
        pass

    def doUpdate(self):
        pass

    def doSelectOne(self):
        pass

def addAndGet():
    a = MailDao()
    test = MailVo(id='1', title='test', contents='testcontents', regDt='a')
    a.doSave(test)


def main():
    a = MailDao()
    test = MailVo(id='1', title='test', contents='testcontents', regDt='a')
    # flag = a.doSave(test)
    flag = a.doDelete(1)
    if flag == 1:
        print("성공")


main()
