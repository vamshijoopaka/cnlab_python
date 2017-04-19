import socket

def encrypt(n):
	en=(n+55)*8
	return en

def decrypt(n):
	dn=(n/7)-10
	return dn

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',2223))
while True:
	inp = input("enter a number:")
	inp1 = encrypt(inp)
	print("encrypted num:"+str(inp1))
	s.send(str(inp1))
	k = s.recv(1024)
	inp1 = int(k)
	k1 = decrypt(inp1)
	print("\treveived :"+k)
	print("\tdecrypted doubled number:"+str(k1))
