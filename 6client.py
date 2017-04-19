import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp=('127.0.0.1',6767)
s.bind(('127.0.0.1',6768))
while True:
        str1=raw_input("ENTER A NUMBER")
        s.sendto(str1,udp)
        if str1=="bye" or str1=="exit":
                print"exiting"
                break
        else:
                data,address=s.recvfrom(1024)
                print"the number is "+str(data)


