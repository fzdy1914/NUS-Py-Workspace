import socket

address = ('3.1.141.4', 53572)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

data = s.recv(512)
print(str(data))

s.close()