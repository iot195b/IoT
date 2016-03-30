import socket
import sys
import mysql.connector 
from mysql.connector import errorcode

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line

server_address = ('', 9801)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
sock.listen(1)

while True:
    try:
    	cnx=mysql.connector.connect(user= 'root',password= 'sheridan1',host= 'localhost',database= 'iot')
    except mysql.connector.Error as e:
    	if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print ("username/password error")
        else:
        	print(e)
    cur= cnx.cursor()
    sql= "SELECT * from relay where id= 1"
    cur.execute(sql)
    results= cur.fetchall()
    for row in results:
	data= row[1]	
    cur.close()
    cnx.close()
    try:
	print >>sys.stderr, 'waiting for a connection'
    	connection, client_address = sock.accept()
        print >>sys.stderr, 'client connected:', client_address
        message = data
    	print >>sys.stderr, 'sending "%s"' % message
    	sock.send(message)
    finally:
	connection.close()