import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',6767))
while True:
        str1=raw_input("ENTER A NUMBER")
        s.send(str1)
        if str1=="bye" or str1=="exit":
                print"exiting"
                break
        else:
                data,address=s.recvfrom(1024)
                print"factorial is"+str(data)

