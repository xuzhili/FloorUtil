import smtplib
from optparse import OptionParser
from email.mime.text import MIMEText


class SendMail:

    def build_mail(self, from_name, to_name, subject, content, from_addr, pwd, to_addr, smtp_server):
        # 构造邮件，内容为hello world
        msg = MIMEText(content)
        # 设置邮件主题
        msg["Subject"] = subject
        # 寄件者
        msg["From"] = from_name
        # 收件者
        msg["To"] = to_name

        from_addr = from_addr
        password = pwd
        # smtp服务器地址
        smtp_server = smtp_server
        # 收件人地址
        to_addr = to_addr
        try:
            # smtp协议的默认端口是25，QQ邮箱smtp服务器端口是465,第一个参数是smtp服务器地址，第二个参数是端口，第三个参数是超时设置,这里必须使用ssl证书，要不链接不上服务器
            server = smtplib.SMTP_SSL(smtp_server, 465, timeout=2)
            # 登录邮箱
            server.login(from_addr, password)
            # 发送邮件，第一个参数是发送方地址，第二个参数是接收方列表，列表中可以有多个接收方地址，表示发送给多个邮箱，msg.as_string()将MIMEText对象转化成文本
            server.sendmail(from_addr, [to_addr], msg.as_string())
            server.quit()
            print('success')
        except Exception as e:
            print('Faild : %s' % e)

    def parse_options(self):
        parser = OptionParser()
        parser.add_option('-f', '--from_name', dest='from_name', help="the name of sender")
        parser.add_option('-t', '--to_name', dest='to_name', help='the name of receiver')
        parser.add_option('-s', '--subject', dest='subject', help='mail subject')
        parser.add_option('-c', '--content', dest='content', help='mail content')
        parser.add_option('-p', '--pwd', dest='pwd', help='password')
        parser.add_option('-r', '--smtp_server', dest='smtp_server', default='smtp.exmail.qq.com', help='smtp server')
        parser.add_option('-a', '--to_addr', dest='to_addr', help='receivers')

        (options, args) = parser.parse_args()

        print("[build.py]options: %s, args: %s" % (options, args))
        return options


if __name__ == '__main__':
    mail = SendMail()
    mail_options = mail.parse_options()
    mail_from = mail_options.from_name
    mail_to = mail_options.to_name
    mail_subject = mail_options.subject
    mail_content = mail_options.content
    mail_pwd = mail_options.pwd
    mail_smtp_server = mail_options.smtp_server
    mail_to_addr = mail_options.to_addr.split(',')

    mail.build_mail(mail_from, mail_to, mail_subject, mail_content, mail_from, mail_pwd, mail_to_addr, mail_smtp_server)
