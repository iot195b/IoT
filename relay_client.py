import RPi.GPIO as GPIO, time
import urllib2
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
true = 1

while(true):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    	server_address = ('54.191.150.101', 9801)
    	sock.connect(server_address)
	try:
		while True:
        		data = connection.recv(16)
			print data
        		break
    	finally:
        	try:
                	if data=='ON':
                		GPIO.output(18,True)
				time.sleep(0.2)
				GPIO.output(18,False)
                	elif data=='OFF':
                		GPIO.output(23,True)
				time.sleep(0.2)
				GPIO.output(23,False)
			else: print 'error'
