import socket

def encrypt(n):
	en=(n+10)*7
	return en

def decrypt(n):
	dn=(n/8)-55
	return dn

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',2223))
s.listen(5)
client,address=s.accept()
while True:
	str1=client.recv(1024)
	out=int(str1)
	out1 = decrypt(out)
	print("recieved:"+str(out1))
	out2 = encrypt(out1*2)
	print("enc at serv:"+str(out2))
	client.send(str(out2))
