import socket
s=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.connect(("192.168.43.136",1011))
while True:
    b=input()
    b=b.encode()
    s.send(b)
    p =s.recv(1024)
    print(p.decode())
