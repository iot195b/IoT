import socket
import time
import sys
import RPi.GPIO as GPIO, time
GPIO.setmode(GPIO.BCM)
pstatus=' '	
# Main program loop
while True:
<<<<<<< HEAD

=======
  
>>>>>>> 65c9ab134fe1cca9e484e7320603984c53fe9c50
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
    if status != pstatus:
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
		#pstatus=status	
		sock.close()
