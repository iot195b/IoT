import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
 
username = "iottoimprovemoderndaylife"
fromaddr = "iottoimprovemoderndaylife@gmail.com"
password = "011235813213455"
toaddr = "himynameisphi@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Contact Switch Alert"
 
body = "Door opened"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, password)
text = msg.as_string()
server.sendmail(username, toaddr, text)
server.quit()
