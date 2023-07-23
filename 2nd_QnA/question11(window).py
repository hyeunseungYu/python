import win32com.client
import pandas as pd

def readAddress(filepath):
    
    file = filepath
    df = pd.read_excel(file)
    
    university_data = df['university']
    email_data = df['email']

    result = pd.DataFrame([university_data,email_data]).T
    
    return result

def sendMail(mail_list):
    outlook = win32com.client.Dispatch("Outlook.Application")
    
    for index, row in mail_list.iterrows():
    # 행 데이터 읽기
        send_mail = outlook.CreateItem(0)
        send_mail.Subject = "[한국투자증권] FY2023 상반기 공개채용 공고 게시 요청"
        send_mail.HTMLBody = row['university']+"커리어개발센터 담당자님 안녕하세요"
        send_mail.To = row['email']
        attachment=r"C:\Users\SamSung\Desktop\sample.xlsx"
        send_mail.Attachments.Add(Source=attachment)
        send_mail.Send()
        
    outlook.Quit()
        

if __name__ =="__main__":
    mailpath= r"C:\Users\SamSung\Desktop\uni_list.xlsx"
    mail_list = readAddress(mailpath)
    sendMail(mail_list)