# coding=utf-8
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import COMMASPACE, formatdate
from email.header import Header
from os.path import basename
import smtplib, os, threading


def send_mail(send_from, send_to, subject, text, files=None):
    assert isinstance(send_to, list)
        
    send_from = str(send_from)
    send_to = [str(item) for item in send_to]
    subject = str(subject)
    text = str(text)

    for file in files or []:
        msg = MIMEMultipart()
        msg['From'] = send_from
        msg['To'] = COMMASPACE.join(send_to)
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject
        msg["Accept-Language"]="zh-CN"
        msg["Accept-Charset"]="ISO-8859-1,utf-8"

        print('Sending %s' % file)
        msg.attach(MIMEText(text, 'plain', 'utf-8'))
        with open(file, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(file)
            )
            part['Content-Disposition'] = 'attachment; filename="%s"' % Header(basename(file), 'utf-8')
            msg.attach(part)

        server = smtplib.SMTP()
        server.connect('smtp.qq.com')
        server.login('251057642', '')
        server.sendmail(send_from, send_to, msg.as_string())
        server.close()

def mutitaskSend(file):
    send_mail('钟少奋<251057642@qq.com>', 
        ['zhongshaofen2012_47@kindle.cn', 
        'zhongshaofen2012_18@kindle.cn'
        ], 
        '文件 %s 到 Kindle' % file, 
        str(file), 
        [file])

allFiles = os.listdir('.')
pdfFiles = filter(lambda path: path.endswith('.pdf') and os.path.getsize(path) < 44 * 1024 * 1024, allFiles)
# bigFiles = filter(lambda path: path.endswith('.pdf') and os.path.getsize(path) > 44 * 1024 * 1024, allFiles)
uploadFile = pdfFiles[0:10]#['当前目录.txt']##


threadPool = []
for file in uploadFile:
    thread = threading.Thread(target=mutitaskSend, args=(file,), name='Send Mail')
    thread.start()
    threadPool.append(thread)

for thread in threadPool:
    thread.join()

print 'Send Success'







