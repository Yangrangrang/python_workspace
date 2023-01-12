'''
JSON data Parse
'''
import os
import sys

import urllib.parse
import urllib.request
import json     # json lib


def json_naver():
    client_id = 'C5MEwWumJxvtV42mGSKB'  # client id
    client_secret = 'BfAruF6ybQ'        # client secret (비번)

    try:
        # 검색어 입력
        search_word = input("검색어를 입력하세요>")
        print('before search_word:{}'.format(search_word))
        # 검색어 : 웹에서 처리 가능하도록 변환
        search_word = urllib.parse.quote(search_word)
        print('after search_word:{}'.format(search_word))
        url = "https://openapi.naver.com/v1/search/blog?query=" + search_word

        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)  #client_id
        request.add_header("X-Naver-Client-Secret", client_secret)  # client_secret

        # naver developer 호출
        response = urllib.request.urlopen(request)

        rescode = response.getcode()
        if 200 == rescode:  # 조회성공
            # encoding UTF-8
            response_body = response.read()
            response_body = response_body.decode('UTF-8')
            print('response_body:{}'.format(response_body))
            return response_body

        else:
            print("실패코드:{}".format(rescode))
            return ""
        # print('response:{}'.format(response.getcode()))

    except Exception as e:
        print("-"*35)
        print(e)
        print("-"*35)


def main():
    # json 문자열 return
    jsonData = json_naver()

    # json 문자열을 Json Object 변환
    jsonObject = json.loads(jsonData)

    # total
    print('total:{}'.format(jsonObject.get("total")))

    # items 실제데이터
    # print('items:{}'.format(jsonObject.get("items")))
    items = jsonObject.get("items")

    for line in items:
        print('title:', line['title'],end=" ")
        print('bloggername:', line['bloggername'],end=" ")
        print('postdate:', line['postdate'])


main()
