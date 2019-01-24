import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = 'SMTP SERVER'
port = 587
usr = 'USER NAME'
pwd = 'PASSWORD'
sender = 'SENDER'
email_list = open('list.txt', 'r')  #IN A SAME DIRECTORY, MAKE A .TXT FILE AND ENTER YOUR EMAIL ADDRESS 1 PER LINE


server = smtplib.SMTP(host, port)
server.starttls()
server.login(usr, pwd)
msg = MIMEMultipart('alternative')
msg['Subject'] = 'SUBJECT'
msg['From'] = sender
plaint_text = ' Test Message'
html_txt = """\


 >>>> YOUR HTML CODE GOES HERE!! <<<<


"""
part1 = MIMEText(plaint_text, 'plain')
part2 = MIMEText(html_txt, 'html')
msg.attach(part1)
msg.attach(part2)
for emails in email_list:
    server.sendmail(sender, emails, msg.as_string())
server.close()
