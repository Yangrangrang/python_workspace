'''
파일명 : p10_03_SQLITE.py
설 명 : 
생성일 : 2023/01/13
생성자 : yanghanna
'''
import sqlite3

def connect():
    conn = None
    try:
        conn = sqlite3.connect("test.db")
    except Exception as e:
        print('-' * 35)
        print('connect:{}'.format(e))
        print('-' * 35)
    return conn

def doUpdate(id, name, content):
    '''update'''

    conn = None
    try:
        conn = connect()
        cur = conn.cursor()
        sql =   '''
                UPDATE FSS_DIC
                SET     name=?
                        ,content=? 
                WHERE id=?;
                '''
        print('sql:{}'.format(sql))
        print('param:{},{},{}'.format(name,content,id))
        cur.execute(sql, (name,content,id))

        # 트랜젼션이 발생 : insert, update, delete
        conn.commit()
        print('트랜잭션 commit')

    except Exception as e:
        print('-' * 35)
        print('connect:{}'.format(e))
        print('-' * 35)
    finally:
        conn.close()




def getCount(name):
    conn = None
    try:
        conn = connect()
        cur = conn.cursor()
        sql = '''
                SELECT count(*)
                FROM FSS_DIC 
                WHERE NAME like ? '''
        print('sql:{}'.format(sql))
        print('param:{}'.format(name))
        cur.execute(sql, ('%'+name+'%',))

        for row in cur:
            print('row:{}'.format(row))

    except Exception as e:
        print('-' * 35)
        print('getCount:{}'.format(e))
        print('-' * 35)
    finally:
        conn.close()

def getCountLike(key):
    '''건수 확인'''
    conn = None
    try:
        conn = connect()
        cur = conn.cursor()
        sql = '''
        SELECT * 
        FROM FSS_DIC 
        WHERE NAME like ? '''

        print('sql:{}'.format(sql))
        print('param:{}'.format(key))
        cur.execute(sql, ('%'+key+'%', ))

        for row in cur:
            print('row:{}'.format(row))

    except Exception as e:
        print('-'*35)
        print('getCount:{}'.format(e))
        print('-'*35)
    finally:
        conn.close()

    print('getCount() 정상 수행')

def doSeleteOne(id):
    '''단건 조회'''
    conn = None # None의미가 자바로 치면 null
    try:
        #1.db 연결 : test.db 없으면 생성, 있으면 생성하지 않는다.
        conn = sqlite3.connect("test.db")

        #2. cursor 생성
        cur = conn.cursor()

        #3. sql문
        sql = "SELECT * FROM FSS_DIC WHERE id=?"
        print('sql:{}'.format(sql))
        print('param:{}'.format(id))

        #4. sql 수행
        cur.execute(sql, (id, ))

        # for row in cur:
        #     print('row:{}'.format(row))

        print('cur.fetchone():{}'.format(cur.fetchone()))


    except Exception as e:
        print('-'*35)
        print('doSeleteOne:{}'.format(e))
        print('-'*35)
    finally:
        conn.close()

    print("doSeleteOne 수행 완료")

def main():
    doSeleteOne(1)
    # getCountLike('휴면')
    # getCount('예금')
    doUpdate(1, '테스트합니다', '수정테스트 완료')
    doSeleteOne(1)

main()
