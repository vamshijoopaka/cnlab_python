import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp=('127.0.0.1',6768)
s.bind(('127.0.0.1',6767))
while True:
	str1,address=s.recvfrom(1024)
	if str1=="bye" or str1=="exit":
		print"exiting"
		break
	else:
		num=int(str1)
		if num%2==0:
			s.sendto("even",udp)
		else:
			s.sendto("odd",udp)
