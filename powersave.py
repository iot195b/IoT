import RPi.GPIO as GPIO, time
GPIO.setmode(GPIO.BCM)
import socket
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

# Main program loop
while True:

    measurement = 0
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, GPIO.LOW)
    GPIO.setup(4,GPIO.OUT)
    time.sleep(0.1)
    GPIO.setup(17, GPIO.IN)
    while (GPIO.input(17) == GPIO.LOW):
    	measurement += 1
    #print measurement
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('54.191.150.101', 9804)
    sock.connect(server_address)
    data = sock.recv(16)
    #print "Power save status  %s" %data 
    if data== 'on' and measurement <1000:
	sock.send("off")
   
			


  
