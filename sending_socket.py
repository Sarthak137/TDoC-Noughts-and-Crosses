import socket

sock = socket.socket(family=socket.AF_INET , type=socket.SOCK_DGRAM)

ip = socket.gethostname()
port=8000

sock.bind(ip,port)
print("Running on",ip,port)

msg="ping"
print("sending:",mesg)

sock.sendto(str("pong").encode('utf-8'),(ip,8000))
recieved_msg = sock.recv(1024).decode('utf-8')

print("recieved_msg",recieved_msg)