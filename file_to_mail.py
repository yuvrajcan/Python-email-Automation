# password : 'evpkkheiyjmwvmfn'
from email.mime import multipart
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
my_email = 'yuvishekhawat345@gmail.com'
password = 'evpkkheiyjmwvmfn'
s= smtplib.SMTP(host='smtp.gmail.com', port = 587)
s.starttls()
s.login(my_email,password)
msg = MIMEMultipart()
msg['From'] = my_email
msg['To'] = input("Enter the email address of the receiver : ")
msg['Subject'] = input("Enter the subject of the mail : ")
body = input("Enter the body of the mail : ")
msg.attach(MIMEText(body, 'plain'))
with open('file.pdf','rb')as file:
    msg.attach(MIMEApplication(file.read(), Name = 'file.pdf'))
s.send_message(msg)
print("Mail sent")
