'''
naver smtp
'''

import smtplib
from email.mime.text import MIMEText

def naver_smtp():
    smtpName = "smtp.naver.com" # SMTP 서버명
    smtpPort = 587              # SMTP 포트

    sendEmail = "gkssk2309@naver.com"   # 네이버 계정
    password = "As7036811*"
    recvEmail = "yhnn2131@naver.com"    # 받는 사람 이메일

    title = "안녕하세요"
    contents = "즐거운 목요일 입니다."

    msg = MIMEText(contents)
    msg['From'] = sendEmail # 보내는 사람
    msg['To'] = recvEmail   # 받는 사람
    msg['Subject'] = title  # 제목

    s = smtplib.SMTP(smtpName,smtpPort) # SMTP서버명, SMTR 포트
    s.starttls()
    s.login(sendEmail,password) # 본인 네이버 계정, 비번
    s.sendmail(sendEmail,recvEmail,msg.as_string())
    s.close()



def main():
    naver_smtp()



main()
