'''
파일명 : p10_01_financedic.py
설 명 : 금융용어 사정 : https://fine.fss.or.kr/main/fin_tip/dic/financedic.jsp
생성일 : 2023/01/13
생성자 : yanghanna
'''
import re   # 검색을 할 때, 좀 더 효율적으로
import sqlite3  # DB
import requests # html 요청
from bs4 import BeautifulSoup

def financedic():
    '''금융용어 사전 스크래핑'''
    fdic = {}   # 키 벨류 형태로 꺼내기 위해
    list_a = []
    list_b = []

    url = "https://fine.fss.or.kr/main/fin_tip/dic/financedic.jsp"    # 금융용어 사이트 url
    try:
        response = requests.get(url)
        print('response.status_code:{}'.format(response.status_code))

        if response.status_code == 200:
            # print('response.text:{}'.format(response.text))
            html = response.text    # html text를 담고 있다
            soup = BeautifulSoup(html, 'html.parser')
            ul = soup.select_one('ul.dic_result_list')  # 용어 리스트 전체
            # print('ul:{}'.format(ul.text))
            # print('ul:{}'.format(ul))

            # 제목
            sub = ul.select('li>dl>dt')
            # print('sub:{}'.format(sub))

            # 내용
            con = ul.select('li>dl>dd')
            # print('con:{}'.format(con))

            for i in sub:
                # print(i.getText())
                # 538. 휴면예금 :  538. 를 지우자 -> 휴면예금
                tmp = i.getText()
                tmp = re.sub('^[0-9]+.','',tmp) # +의 의미는 1개 이상
                # print(tmp)
                tmp = tmp.replace("\r\n\t\t\t\t\t\t\t\t\xa0","")
                tmp = tmp.strip()
                # print(tmp)

                list_a.append(tmp)

            for i in con:
                tmp = i.getText()   # getText : text만 꺼내라
                list_b.append(tmp)

            # print(list_a)
            # print(list_b)

            # 키: 벨류 형태(딕셔너리)로 fdic에 넣을 것
            for i in range(len(list_a)):
                # print(i, end=" ")
                fdic[i] = [list_a[i], list_b[i]]

            print('fdic:{}'.format(fdic))

        else:
            print('response.status_code:{}'.format(response.status_code))
            print("url을 확인 하세요.")
    except Exception as e:
        print(e)


def main():
    financedic()


main()
