import socket                
  
s = socket.socket()      
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)     
port = 10101               
  
s.bind(('', port))          
s.listen(5)     

while True:
	c, addr = s.accept()      
	print('Got connection from', addr)
  
	# receive data from the server 
	prime = c.recv(2048).decode('ascii')
	generator = c.recv(2048).decode('ascii')
	public_key = c.recv(2048).decode('ascii')

	print(prime, generator, public_key)

	message = c.recv(2048).decode('ascii')

	signature = c.recv(4096).decode('ascii')
	print("Received message and signature : ")
	print(message, signature)
	# close the connection 
	s.close()        