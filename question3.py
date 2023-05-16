import smtplib
from email.message import EmailMessage

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
email_addr = "hyeunseung03@gmail.com"
email_pass = "tdiknxllcgmptcxh"

def send_email(email_addr, to_name):
    smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    smtp.login(email_addr, email_pass)

    message = EmailMessage()
    message.set_content("금일 해외배당내역드립니다. 감사합니다.")
    message["Subject"] = "[KIS] TRS Dividend_20230516"
    message["From"] = email_addr
    message["To"] = to_name

    report_file = "filtered_data_by_ticker_20230515.pdf"
    with open(report_file, "rb") as f:
        file_data = f.read()
        message.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=report_file)

    smtp.send_message(message)
    smtp.quit()

send_email(email_addr,'ackrite03@naver.com')