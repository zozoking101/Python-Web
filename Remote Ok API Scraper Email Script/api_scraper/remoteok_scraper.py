import requests
import xlwt
from xlwt import Workbook
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

BASE_URL = "https://remoteok.com/api/"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
REQUEST_HEADER = {
    'User-Agent': USER_AGENT,
    # 'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Referer': 'https://remoteok.com/',
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'X-Requested-With': 'XMLHttpRequest',
    # 'Connection': 'keep-alive',
}

def get_job_postings():
    res = requests.get(url = BASE_URL, headers= REQUEST_HEADER)
    return res.json()

def output_job_to_xls(data):
    wb = Workbook()
    job_sheet = wb.add_sheet('Jobs')
    headers = list(data[0].keys())
    for i  in range(0, len(headers)):
        job_sheet.write(0, i, headers[i]) 
    for i in range(1, len(data)):
        for j in range(len(headers)):
            job_sheet.write(i, j, data[i][headers[j]])
        # OR
        # job = data[i]
        # values = list(job.values()) # slug company location epoch salary
        
        # job_sheet.write(i, j, values[j])
    wb.save('remote_jobs.xls')

def send_email(send_from, send_to, subject, text, files=None):
    assert isinstance(send_to, list)
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    
    msg.attach(MIMEText(text))
    
    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        part['Content-Disposition'] = f'attachment; filename="{basename(f)}"'
        msg.attach(part)
    try:    
        smtp = smtplib.SMTP('smtp.mail.yahoo.com', 587)
        # smtp.starttls()
        smtp.login(send_from, 'txhlgwbjbojmhist') #
        smtp.sendmail(send_from, send_to, msg.as_string())
        smtp.quit()
        print('Sent mail')
    except Exception as e:
        print(f'{e}: Can\'t send the email.')

if __name__ == '__main__':
    json = get_job_postings()[1:]
    output_job_to_xls(json)
    send_email('evilestminion25@yahoo.com', 
               ['zoe.oladokun@gmail.com'], 
               'Job Postings', 
               'Please, find attached a list of job postings in this email.',
               files=['remote_jobs.xls']
               )
    