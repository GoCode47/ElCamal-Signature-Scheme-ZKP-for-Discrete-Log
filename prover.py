import socket
from utils import get_safe_prime_and_generator
from utils import generate_keys   
from utils import sign 


# Create a socket object 
s = socket.socket()          
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Define the port on which you want to connect 
port = 10101                
  
# connect to the server on local computer 
s.bind(('', port))
s.connect(('127.0.0.1', port)) 

#no of bits of security
k = 8                   

#use pre-computed safe prime and generator or generate the pair
#prime, generator = 2337337002729225098572093778426340936344769375016804739, 408301515976774063741225363930200775333880949653971216
prime, generator = get_safe_prime_and_generator(k)
keys = generate_keys(prime,generator)

s.send(str(prime).encode('ascii'))
s.send(str(generator).encode('ascii'))
s.send((str(keys['public_key'])).encode('ascii'))

print('Enter message to apply signature to : ')
message = input()
s.send(str(message).encode('ascii'))

signature = sign(message, keys['secret_key'], prime, generator)
s.send(str(signature).encode('ascii'))

s.close() 