'''
파일명 : p11_02©_logging_format.py
설 명 : logging format file
생성일 : 2023/01/19
생성자 : yanghanna
'''
import logging

def main():
    # 로그 생성
    logger = logging.getLogger()

    # 로그 레벨
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s -%(levelname)s -%(filename)s -%(name)s -%(lineno)d - %(message)s')

    # console log 출력
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # fiel log 출력
    file_handler = logging.FileHandler('my.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    for i in range(10):
        logging.info("{}번째 방문 입니다.".format(i))

main()
