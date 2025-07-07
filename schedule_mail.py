import schedule
import time
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

def send_email():
    s.send_message(msg)
schedule.every(5).seconds.do(send_email)
p=0
while True:
    p+=1
    schedule.run_pending()
    time.sleep(1)
    
print("mail has been sent",p,"times")
    

