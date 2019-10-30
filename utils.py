from random import randrange
from modular_inverse import modInverse
from hashlib import sha256
from math import gcd
from rabin_miller import is_probable_prime
import random

def get_generator_for_safe_prime(p,q):
	completed = False
	while not completed:
		alpha = random.randrange(p-1)
		for exp in [2, q]:
	  		b = pow(alpha,(p-1)//exp, p)
	  		tmp = b % p == 1
	  		if tmp: break
		if not tmp: completed = True
	return alpha

def get_safe_prime(k):
	while True:
  		q = 2*random.getrandbits(k-1)+1
  		if not is_probable_prime(q): 
  			continue

  		p = 2*q+1
  		if not is_probable_prime(p): 
  			continue
  		return p,q

def get_safe_prime_and_generator(k):
	p,q = get_safe_prime(k)
	g = get_generator_for_safe_prime(p,q)
	return p,g

def generate_keys(p,g):
	x = randrange(2, p-1)
	y = pow(g,x,p)
	return {'secret_key':x,'public_key':y}

def sign(m, x, p, g):
    s = 0
    while s == 0:
        k = randrange(2, p-1)
        while gcd(k, p-1) !=1:
        	k = randrange(2, p-1)
        r = pow(g,k,p)
        s = (int.from_bytes(sha256(m.encode('utf-8')).digest(), 'big') - x*r)*modInverse(k,p-1) % (p-1)
    return r,s

def verify(m, signature_, y):
	r,s = signature_
	assert 0 < r < p and 0 < s < p-1, 'Signature input are not in the right interval.'
	assert pow(g, int.from_bytes(sha256(m.encode('utf-8')).digest(), 'big'), p) == pow(y,r,p)*pow(r,s,p)%p, 'The signature is not valid for the string "{m.decode("utf-8")}".'
	print(f'The signature is valid for the string "{m}"')
	return True