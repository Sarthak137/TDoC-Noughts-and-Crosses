import socket

sock = socket.socket(family=socket.AF_INET , type=socket.SOCK_DGRAM)

ip = socket.gethostname()
port=8001

sock.bind(ip,port)
print("Running on",ip,port)

recieved_msg = sock.recv(1024).decode('utf-8')

if recieved_msg == "ping":
    sock.sendto(str("pong").encode('utf-8'),(ip,8000))
    print("sending:","pong")