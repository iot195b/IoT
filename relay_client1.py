<<<<<<< HEAD:relay_client1.py
import socket
import RPi.GPIO as GPIO, time
import urllib2
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
true = 1
pstatus = ' '
while(true):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    	server_address = ('54.191.150.101', 9801)
    	sock.connect(server_address)
	try:
		while True:
        		data = sock.recv(16)
			status= data 
        		break
    	finally:
                	if data=='on' and pstatus !=status:
				pstatus=status
				print "Device 1 %s" %data
                		GPIO.output(18,True)
				time.sleep(0.2)
				GPIO.output(18,False)
                	elif data=='off' and pstatus != status:
				pstatus=status
				print "Device 1 %s" %data
                		GPIO.output(23,True)
				time.sleep(0.2)
				GPIO.output(23,False)
			
=======
import socket
import RPi.GPIO as GPIO, time
import urllib2
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
true = 1
pstatus = ' '
while(true):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    	server_address = ('54.191.150.101', 9801)
    	sock.connect(server_address)
	try:
		while True:
        		data = sock.recv(16)
			status= data
        		break
    	finally:
                	if data=='on' and pstatus !=status:
                		pstatus =status
                		GPIO.output(18,True)
				time.sleep(0.2)
				GPIO.output(18,False)
                	elif data=='off' and pstatus !=status:
                		pstatus =status
                		GPIO.output(23,True)
				time.sleep(0.2)
				GPIO.output(23,False)
			else: print 'error'
>>>>>>> 65c9ab134fe1cca9e484e7320603984c53fe9c50:relay_client.py
