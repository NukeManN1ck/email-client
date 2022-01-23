import smtplib
from email import encoders, message
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart



server = smtplib.SMTP('smtp.gmail.com',25)

server.ehlo()
server.login('mail@mail.com', 'password1234567890')

# you can also import a .txt file (recommended) ^ if you don't want to 
# write your password or email into your script 
# example: 
# with open('password.txt', 'r') as f:
#     password = f.read()

msg = MIMEMultipart()
msg['From'] = 'mail@mail.com'
msg['To'] = 'elonmusk@hotmail.com'
msg['Subject'] = 'Need Some Money'


with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'muskmeme.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64()
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('mail@mail.com', 'elonmusk@hotmail.com', text)
