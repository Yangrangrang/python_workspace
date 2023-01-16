'''
파일명 : cmn.py
설 명 : CRUD 추상메서드 클래스
생성일 : 2023/01/16
생성자 : yanghanna
'''

from abc import *

class WorkDiv(metaclass=ABCMeta):
    '''DAO 표준 메서드 (CRUD)'''

    @abstractclassmethod
    def doSave(self):
        '''저장'''
        pass

    @abstractclassmethod
    def doDelete(self):
        '''삭제'''
        pass

    @abstractclassmethod
    def doSelectOne(self):
        '''단건조회'''
        pass

    @abstractclassmethod
    def doUpdate(self):
        '''수정'''
        pass

    @abstractclassmethod
    def doRetrieve(self):
        '''목록 조회'''
        pass