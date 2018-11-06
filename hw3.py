import math
import sys
import binascii
import numpy as np

np.set_printoptions(linewidth = 100)

if len(sys.argv) != 5: 
	print "Usage: ./hw1.py <p> <q> <seed> <m>"
	exit()
p = int(sys.argv[1])
q = int(sys.argv[2])
x0 = int(sys.argv[3])
mbits = sys.argv[4]

N = p*q

#encryption
m = np.zeros(len(mbits))
for i in range(0, len(mbits)):
	m[i] = int(mbits[i])

XL = x0
b = np.zeros(len(mbits))
for i in range(0, len(mbits)):
	b[i] = XL%2
	XL = pow(XL, 2, N)

print "encrypting..."
print "message: "
print m
print "random string: "
print b

c = np.zeros(len(mbits))
for i in range(0, len(mbits)):
	c[i] = (m[i] + b[i]) % 2

print "ciphertext: "
print c		

print "decrypting..."
#since this is a public key cryptosystem, alice has access to most variables

rp = (p+1)/4
rq = (q+1)/4
rp = pow(rp, len(mbits))
rq = pow(rq, len(mbits))
rp = pow(XL, rp, p)
rq = pow(XL, rq, q)

#a and b aren't really neccesary inputs, as they can
#be computed easily since p and q are primes
a = pow(p, q-2, q)
b = pow(q, p-2, p)

x0 = (b*q*rp + a*p*rq) % N
#recompute b then m
XL = x0
b = np.zeros(len(mbits))
for i in range(0, len(mbits)):
	b[i] = XL%2
	XL = pow(XL, 2, N)

print "recomputed random string:"
print b
m = np.zeros(len(mbits))
for i in range(0, len(mbits)):
	m[i] = (c[i] + b[i]) % 2

print "decrypted message:"
print m







