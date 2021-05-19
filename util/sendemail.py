import smtplib
from email.message import Message
import urllib.parse
import time
from email.mime.text import MIMEText

class SendEmail():
    def __init__(self):

        self.info = {}
        self.info['name'] = '1832596901@qq.com'
        self.info['password'] = 'ltxsbelcnnfgeeba'
        self.server = smtplib.SMTP('smtp.qq.com', 25)
        self.server.login('1832596901@qq.com', 'ltxsbelcnnfgeeba')

    def Send(self, to='email', sub='title', text='pleace input some thing'):
        Body = '\r\n'.join(
            [f'To: {to}', 'From: {}'.format(self.info['name']), f'Subject: {sub}', '', urllib.parse.quote(text)])
        froms = 'From nobody ' + time.ctime(time.time()) + '\n'
        subs = f'Subject: {sub}\n'
        mfroms = 'From: 1832596901@qq.com\n'
        Tos = f'To: {to}\n'
        Ccs = f'Cc: {to}\n\n'
        msgs = ''.join([froms, subs, mfroms, Tos, Ccs, text])
        print(msgs.encode('utf8'))
        try:
            self.server.sendmail(self.info['name'], to, msgs.encode('utf8'))
            print('send email success')
        except Exception as e:
            print(f'send email error: {e}')

        self.server.quit()

"""
def send_email(content, to_email):
    sender = 'humeng13535324513@gmail.com'
    receiver = to_email
    host = 'smtp.gmail.com'
    port = 587
    msg = Message()
    msg['From'] = 'humeng13535324513@gmail.com'
    msg['To'] = to_email
    msg['Subject'] = 'password reset'
    try:
        smtp = smtplib.SMTP_SSL(host, port)
        smtp.ehlo()  # 向Gamil发送SMTP 'ehlo' 命令
        smtp.starttls()
        smtp.login(sender, 'HM520ll8511561')
        smtp.sendmail(sender, receiver, msg.as_string())
        print('send ok')
    except Exception as e:
        print(e)
"""
def send_email(content, to_email):
    sender = '1832596901@qq.com'
    passwd = 'ltxsbelcnnfgeeba'
    msg = MIMEText(content)
    msg['Subject'] = 'password reset'
    msg['From'] = sender
    msg['To'] = to_email
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com",465)    #邮件服务器及端口号
        s.login(sender, passwd)
        s.sendmail(sender, to_email, msg.as_string())
        print("发送成功")
    except Exception as e:
        print(e)
    finally:
        s.quit()

#if __name__ == '__main__':
    #send_email('你好，哈哈', '13535324513@163.com')
    #s = SendEmail()
    #s.Send('13535324513@163.com','password reset','你好 哈哈')
