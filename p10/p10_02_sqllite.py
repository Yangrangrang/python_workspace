'''
파일명 : p10_02_sqllite.py
설 명 : sqllite3 (기본적으로 설치) 사용 방법
생성일 : 2023/01/13
생성자 : yanghanna
'''

import sqlite3
from sqlite3 import Error   # 예외

def doDelete():
    conn = None
    try:
        # 1. DB 생성 및 연결
        conn = sqlite3.connect("test.db")  # 파일이 생성된 현재 디렉토리에
        # print('db:{}'.format(db))

        # 2. 커서 생성
        cur = conn.cursor()

        # 3. sql 삭제
        sql = "DELETE FROM fss_dic WHERE id = ?"

        # 4. sql 수행 ,param
        # parameters are of unsupported type
        # cur.execute(sql,(1))
        cur.execute(sql,(1,))


        # 5. 트랜잭션
        conn.commit()


    except Exception as e:
        print("-" * 35)
        print(e)
        print("-" * 35)
    finally:
        conn.close()

def doSave():
    conn = None
    try:
        # 1. DB 생성 및 연결
        conn = sqlite3.connect("test.db")  # 파일이 생성된 현재 디렉토리에
        # print('db:{}'.format(db))

        # 2. 커서 생성
        cur = conn.cursor()

        # 3. sql 생성
        sql = "INSERT INTO fss_dic VALUES (?,?,?)"

        # 4. sql 수행 ,param
        cur.execute(sql, (1,'키워드', '내용'))

        # 5. 트랜잭션
        conn.commit()


    except Exception as e:
        print("-"*35)
        print(e)
        print("-"*35)
    finally:
        conn.close()

def main():
    doDelete()

main()
