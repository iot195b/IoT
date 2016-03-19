import socket
import time
import sys
import RPi.GPIO as GPIO, time
GPIO.setmode(GPIO.BCM)
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Main program loop
while True:
    pstatus=' '	
    time.sleep(2)
    measurement = 0
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, GPIO.LOW)
   # GPIO.setup(4,GPIO.OUT)
    time.sleep(0.1)
    GPIO.setup(17, GPIO.IN)
    while (GPIO.input(17) == GPIO.LOW):
        measurement += 1
    #print measurement
    if measurement > 1000:
	status= 'Dark'
    else: 
	status= 'Light'
    if status == pstatus:
	a=b
    else:
	pstatus = status
    	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    	server_address = ('54.191.150.101', 9800)
    	sock.connect(server_address)
    	try:
    		message =status
    		print >>sys.stderr, 'sending "%s"' % message
    		sock.sendall(message)
    		amount_received = 0
    		amount_expected = len(message)
    		#while amount_received < amount_expected:
			#data = sock.recv(16)
			#amount_received += len(data)
			#print >>sys.stderr, 'received "%s"' % data
		data = sock.recv(16)
		print data;
    	finally:
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
		#pstatus=status	
		sock.close()