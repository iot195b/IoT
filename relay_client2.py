import socket
import RPi.GPIO as GPIO, time
import urllib2
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
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
				print "Device 2 %s" %data
                		GPIO.output(20,True)
				time.sleep(0.2)
				GPIO.output(20,False)
                	elif data=='off' and pstatus != status:
				pstatus=status
				print "Device 2 %s" %data
                		GPIO.output(21,True)
				time.sleep(0.2)
				GPIO.output(21,False)
			
