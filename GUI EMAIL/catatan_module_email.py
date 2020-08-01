import os
import smtplib
import imghdr
from email.message import EmailMessage
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
EMAIL_TO = "terkerenos123@gmail.com"

# debugg ##
# smtp =  smtplib.SMTP('localhost',1026) --> ini command untuk debugging. dan tanpa lainnya
# python -m smtpd -c DebuggingServer -n localhost:1026 --> untuk debugging melalui localhost.

# without ssl ##
smtp =  smtplib.SMTP('smtp.gmail.com',587)
smtp.ehlo() # sending 
smtp.starttls() # encript sending
smtp.ehlo() # verification u are sending 

msg = EmailMessage()
msg['Subject'] = "Check this attachment can help u or not ?"
msg['From'] = EMAIL_ADDRESS 
msg['To'] = ", ".join(EMAIL_TO)# can send multiple email with sperated " , "
msg.set_content(" This file for u learn UAS in the school...") # body 


## sendding attachment :
with open("LATIHAN SOAL UAS KD 3.4.pdf",'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name
# file1 = open('text_lists.txt',"r")
# lines = file1.readlines()
# for f in lines:
msg.add_attachment(file_data, maintype='application', subtype= "octet-stream", filename= file_name)
# msg.add_attachment(file_data, maintype='image', subtype= file_type, filename= file_name) --> for sendding imagers
# msg.add_attachment(file_data, maintype='application', subtype= "octet-stream", filename= file_name) --> for sendding PDF or other file

## sendding email with HTML format 
# msg.add_alternative("""\
#     <!DOCTYPE html>
# <html>
#     <body>
#         <h1 style="color:cyan">This is my HTML massage for u !</h1>
#     </body>
# </html>

# """, subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)



## file1 = open('text_lists.txt',"r")
## lines = file1.readlines()
## print(lines)
