import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',5555))
n=raw_input()
s.send(n)
k=s.recv(1024)
print k
n=raw_input()
s.send(n)
k=s.recv(1024)
print k

