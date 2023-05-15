import smtplib
from email.message import EmailMessage

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)


email_addr = "hyeunseung03@gmail.com"
email_pass = "tdiknxllcgmptcxh"


smtp.login(email_addr, email_pass)

message = EmailMessage()
message.set_content("이메일 본문")
message["Subject"] = "이메일 제목"
message["From"] = email_addr
message["To"] = "hyeunseung03@gmail.com"

smtp.send_message(message)
smtp.quit()