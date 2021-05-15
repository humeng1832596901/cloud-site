import smtplib
from email.message import Message
import urllib.parse
import time


class SendEmail():
    def __init__(self):

        self.info = {}
        self.info['name'] = 'xxx@gmail.com'
        self.info['password'] = 'xxx' #邮箱密码
        self.server = smtplib.SMTP('smtp.gmail.com', 25) #SSL连接不稳定，直接换成原生SMTP协议
        self.server.ehlo_or_helo_if_needed()
        self.server.starttls()
        self.server.login(self.info['name'], self.info['password'])

    def Send(self, to='email', sub='title', text='pleace input some thing'):
        Body = '\r\n'.join(
            [f'To: {to}', 'From: {}'.format(self.info['name']), f'Subject: {sub}', '', urllib.parse.quote(text)])
        froms = 'From nobody ' + time.ctime(time.time()) + '\n'
        subs = f'Subject: {sub}\n'
        mfroms = 'From: xxxx@gmail.com\n'    #你的邮箱
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


def send_email(content, to_email):
    sender = 'xxx@gmail.com'    #你的邮箱
    receiver = to_email
    host = 'smtp.gmail.com'
    port = 25
    msg = Message()
    msg['From'] = 'xxx@gmail.com'  #你的邮箱
    msg['To'] = to_email
    msg['Subject'] = 'yuncluod.com'
    try:
        smtp = smtplib.SMTP(host, port)
        smtp.ehlo()  # 向Gamil发送SMTP 'ehlo' 命令
        smtp.starttls()
        smtp.login(sender, 'xxx') #这里填写gmail密码
        smtp.sendmail(sender, receiver, msg.as_string())
        print('send ok')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    #如果还不行记得把谷歌的二级验证关掉
    send_email('你好，哈哈', 'xxx') #这里填写测试邮箱
