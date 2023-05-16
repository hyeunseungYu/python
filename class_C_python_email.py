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



###############################################

SMTP_PORT = 465
email_addr = "email5678@gmail.com"
email_pass = "abcdefghijklmnop"

def send_email(email_addr, to_name):
	smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
	smtp.login(email_addr, email_pass)

	message = EmailMessage()
	message.set_content("이메일 본문")
	message["Subject"] = "이메일 제목"
	message["From"] = email_addr
	message["To"] = "보낼 이메일 주소"

	report_file = "report.pdf"
	with open(report_file, "rb") as f:
		file_data = f.read()
		message.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=report_file)

	smtp.send_message(message)
	smtp.quit()
