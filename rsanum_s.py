import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',5555))
s.listen(5)
client,addr=s.accept()
#k=client.recv(1024)
#k=int(k)
temp=client.recv(1024)
pub_key=temp.split('-')
e=int(pub_key[0])
n=int(pub_key[1])
c=1
k=client.recv(1024)
k=int(k)*2
for l in range(0,e):
	c*=k
	c%=n
c%=n
client.send(str(c))
