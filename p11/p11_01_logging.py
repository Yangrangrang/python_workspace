'''
파일명 : p11_01_logging.py
설 명 : 
생성일 : 2023/01/19
생성자 : yanghanna
'''
import logging

def main():
    logging.basicConfig(level=40)

    logging.debug('debug message')
    logging.info('info message')
    logging.warning('warning message')
    logging.error('error message')
    logging.critical('critical message')


main()
