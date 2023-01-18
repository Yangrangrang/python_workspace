'''
파일명 : service_addressbook.py
설 명 : addressbook service
생성일 : 2023/01/17
생성자 : yanghanna
'''

from vo import Member
from dao_addressbook import AddressbookDao
import smtplib
from email.mime.text import MIMEText
from mail.dao_mail import MailDao
from mail.vo_mail import MailVo

class AddressbookService:
    def __init__(self):
        self.dao = None

    def doSelectOne(self,member:Member):
        '''단건 조회'''
        self.dao = AddressbookDao() # dao 객체 생성
        # ID 입력
        print('doSelectOne.id:{}'.format(member.id))
        outVo = self.dao.doSelectOne(m=member)
        return outVo

    def doDelete(self,member:Member):
        '''단건 삭제'''
        self.dao = AddressbookDao()
        return self.dao.doDelete(member.id)

    def doSave(self,member:Member):
        '''등록'''
        self.dao = AddressbookDao()
        return self.dao.doSave(member)

    def doUpdate(self,member:Member):
        '''수정'''
        self.dao = AddressbookDao()
        return self.dao.doUpdate(member)

    def doRetrieve(self,searchDiv,searchWord):
        '''목록 조회'''
        self.dao = AddressbookDao()
        return self.dao.doRetrieve(searchDiv,searchWord)

    def doSendMail(self, searchDiv, searchWord):
        '''목록조회'''
        '''
            mail_contents 테이블 내용을 불러온다.
                - 제목, 내용
            addressbook의 모든 사용자를 불러온다.
                - name, receiv_email
        '''
        self.daoMail = MailDao()
        self.mailVO = MailVo()
        self.mailVO.id = 1

        outMail = self.daoMail.doSelectOne(self.mailVO)
        print('outMail:{},{},{},{}'.format(outMail.id, outMail.title, outMail.contents, outMail.regDt))

        self.dao = AddressbookDao()
        listMember = self.dao.doRetrieve(searchDiv,searchWord)

        for m in listMember:
            print('m:{},{},{},{}'.format(m.id, m.name, m.passwd, m.email))
            self.naver_smtp(name=m.name, receiv_email=m.email, p_title=outMail.title, p_contents=outMail.contents)
        pass

    def naver_smtp(self, name, receiv_email, p_title, p_contents):
        s = None
        try:
            smtpName = "smtp.naver.com"  # SMTP 서버명
            smtpPort = 465  # SMTP 포트

            sendEmail = "gkssk2309@naver.com"  # 네이버 계정
            password = "yhnn2131*"
            recvEmail = receiv_email  # 받는 사람 이메일

            title = p_title
            contents = '{}님 \n {}'.format(name, p_contents)

            msg = MIMEText(contents)
            msg['From'] = sendEmail  # 보내는 사람
            msg['To'] = recvEmail  # 받는 사람
            msg['Subject'] = title  # 제목

            s = smtplib.SMTP_SSL(smtpName, smtpPort)  # SMTP서버명, SMTR 포트
            s.set_debuglevel(True)  # 465/ SMTP_SSL
            # s.starttls() #587
            s.login(sendEmail, password)  # 본인 네이버 계정, 비번
            s.sendmail(sendEmail, recvEmail, msg.as_string())
        except Exception as e:
            print(e)
        finally:
            if s is not None:
                s.close()

def main():
    if __name__ == '__main__':
        a = AddressbookService()
        outVo = a.doSendMail(searchDiv='',searchWord='')



main()
