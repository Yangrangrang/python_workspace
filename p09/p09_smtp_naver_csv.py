'''
naver smtp
'''

import smtplib
from email.mime.text import MIMEText

def naver_smtp(name, receiv_email, p_title, p_contents):
    s = None
    try:
        smtpName = "smtp.naver.com" # SMTP 서버명
        smtpPort = 465              # SMTP 포트

        sendEmail = "gkssk2309@naver.com"   # 네이버 계정
        password = "As7036811*"
        recvEmail = receiv_email   # 받는 사람 이메일

        title = p_title
        contents = '{}님 \n {}'.format(name, p_contents)

        msg = MIMEText(contents)
        msg['From'] = sendEmail # 보내는 사람
        msg['To'] = recvEmail   # 받는 사람
        msg['Subject'] = title  # 제목

        s = smtplib.SMTP_SSL(smtpName,smtpPort) # SMTP서버명, SMTR 포트
        s.set_debuglevel(True)  # 465/ SMTP_SSL
        # s.starttls() #587
        s.login(sendEmail,password) # 본인 네이버 계정, 비번
        s.sendmail(sendEmail,recvEmail,msg.as_string())
    except Exception as e:
        print(e)
    finally:
        if s is not None:
            s.close()

def read_csv():
    try:
        #
        with open("email_list.csv", "r") as f:
            mail_list = [] # csv파일 한줄씩 담기
            i = 0
            while True:
                line = f.readline()
                if not line:
                    break
                else:
                    print(line)
                    mail_list.append(line.strip("\n"))  # 리스테 한줄 추가, \n 제거
            return  mail_list
    except IOError as e:
        print("-"*35)
        print(e)
        print("-"*35)
    finally:
        print("완료")

def main():

    mail_list = read_csv()
    list_str = []
    for m_list in mail_list[1:]:
        list_str = m_list.split(",")
        naver_smtp(name=list_str[1], receiv_email=list_str[2], p_title=list_str[3], p_contents=list_str[4])


main()
