import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ipmac={}
f=open("arp.txt",'r')
for k in f.readlines():
	if ',' not in k:
		continue
	l=k.split(',')
	ipmac[l[0]]=l[1][:-1]
#print ipmac

s.bind(('127.0.0.1',5555))
s.listen(5)
client,addr=s.accept()
k=client.recv(1024)
client.send(ipmac[k])
k=client.recv(1024)
for l in ipmac.keys():
	if ipmac[l]==k:
		client.send(l)

s.close()
