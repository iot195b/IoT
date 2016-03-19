import RPi.GPIO as GPIO, time
import urllib2
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
true = 1

while(true):
                try:
                        response = urllib2.urlopen('http://ec2-54-191-150-101.us-west-2.compute.amazonaws.com/buttonStatus.php')
                        status = response.read()
                except urllib2.HTTPError, e:
                                        print e.code

                except urllib2.URLError, e:
                                        print e.args

                #print status
                if status=='ON':
                                GPIO.output(18,True)
				time.sleep(0.2)
				GPIO.output(18,False)
                elif status=='OFF':
                                GPIO.output(23,True)
				time.sleep(0.2)
				GPIO.output(23,False)

						
		else: print 'error'
