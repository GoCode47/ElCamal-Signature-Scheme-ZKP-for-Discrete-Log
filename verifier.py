import socket
from utils import verify                
  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)     
port = 11111              
  
s.bind(('', port))          
s.listen(5)     

while True:
	c, addr = s.accept()      
	print('Got connection from', addr)

	complete_message = c.recv(2048).decode('ascii')
	#print(complete_message)
  
	# receive data from the prover
	prime, generator, public_key, message, signature = complete_message.split('/')
	prime = int(prime)
	generator = int(generator)
	public_key = int(public_key)
	signature = eval(signature)
	
	print("Received Message : ", message)
	print("Received Signature : ", signature)
	
	print("Verifying the signature...")
	verify(message, signature, public_key, prime, generator)
	
	c.close()        
