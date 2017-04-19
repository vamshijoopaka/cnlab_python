import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',6789))
s.listen(5)
client,address=s.accept()
while True:
	str1=client.recv(1024)
	if str1=="bye" or str1=="exit":
		print"exiting"
		break
	else:
		num=int(str1)
		num=num**3
		str1=str(num)
		client.send(str1)

