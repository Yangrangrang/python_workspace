'''
파일명 : p11_04_logger_config.py
설 명 : 
생성일 : 2023/01/19
생성자 : yanghanna
'''
import logging
import logging.config
import json
import os

# with 자동으로 close
with open('logging.json', 'rt') as f:
    config = json.load(f)

    logging.config.dictConfig(config)
    logger = logging.getLogger()

    for i in range(10):
        logger.info("loggin.json test!")
