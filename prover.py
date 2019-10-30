import socket
from utils import get_safe_prime_and_generator
from utils import generate_keys   
from utils import sign 


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

port = 11111                
  
# connect to the verifier 
s.connect(('127.0.0.1', port)) 

#no of bits of security
k = 8                   

#use pre-computed safe prime and generator or generate the pair
#prime, generator = 2337337002729225098572093778426340936344769375016804739, 408301515976774063741225363930200775333880949653971216
prime, generator = get_safe_prime_and_generator(k)
keys = generate_keys(prime,generator)

print('Enter message to apply signature to : ')
message = input()

signature = sign(message, keys['secret_key'], prime, generator)

complete_message = str(prime)+'/'+str(generator)+'/'+str(keys['public_key'])+'/'+message+'/'+str(signature)
s.send(complete_message.encode('ascii'))

s.close() 
