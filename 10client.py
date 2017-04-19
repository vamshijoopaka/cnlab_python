import socket 
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',6789))
while True:
	str1=raw_input("enter a number")
	s.send(str1)
	if str1=="bye" or str1=="exit":
		print"exiting"
		break
	else:
		data=s.recv(1024)
		print"cube of the numbe is"+str(data)
	
