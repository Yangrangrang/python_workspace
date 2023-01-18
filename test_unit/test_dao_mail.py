import unittest

from mail.vo_mail import MailVo
from mail.dao_mail import MailDao

class MailTest(unittest.TestCase):
    '''unitest 라이프 사이클'''

    def setUp(self) -> None:
        print("0.setUp------------>")
        print("테스트 픽처스: 테스트 데이터 초기화")
        self.m01 = MailVo(id=1,title='smtp mail 테스트', contents='오늘은 즐거운 날', regDt='202301181000')
        self.m02 = MailVo(id=2,title='smtp mail 테스트20', contents='오늘은 즐거운 날20', regDt='202301181000')
        self.m03 = MailVo(id=3,title='smtp mail 테스트30', contents='오늘은 즐거운 날30', regDt='202301181000')
        self.dao = None

    def tearDown(self) -> None:
        print("99.tearDown------------>")
        print("자원 반납")

    '''테스트 메서드는 test_이름'''
    def test_addAndGet(self):
        print('1. test_addAndGet()**********')
        # 1. 기존 데이터 삭제
        # 2. 데이터 등록
        # 3. 데이터 조회
        # 4. 조회데이터 등록데이터 비교

        self.dao = MailDao()

        self.dao.doDelete(self.m01.id)
        self.dao.doDelete(self.m02.id)
        self.dao.doDelete(self.m03.id)

        flag = self.dao.doSave(self.m01)
        self.assertEqual(flag, 1)

        flag = self.dao.doSave(self.m02)
        self.assertEqual(flag, 1)

        flag = self.dao.doSave(self.m03)
        self.assertEqual(flag, 1)


        outVO01 = self.dao.doSelectOne(self.m01)
        outVO02 = self.dao.doSelectOne(self.m02)
        outVO03 = self.dao.doSelectOne(self.m03)
        # self.assertIsNotNone(outVO)
        self.isSameData(self.m01, outVO01)
        self.isSameData(self.m02, outVO02)
        self.isSameData(self.m03, outVO03)

    def isSameData(self,orgMail,vsMail):
        self.assertEqual(orgMail.id,vsMail.id)
        self.assertEqual(orgMail.title,vsMail.title)
        self.assertEqual(orgMail.contents,vsMail.contents)
        self.assertEqual(orgMail.regDt,vsMail.regDt)

    @unittest.skip('테스트 연습')
    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')

    @unittest.skip('건너뛰기 테스트')
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertTrue('foo'.isupper())

if __name__ == '__main__':
    unittest.main()
