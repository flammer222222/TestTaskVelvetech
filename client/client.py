import socket

sock = socket.socket()
sock.connect(('localhost', 9080))
sock.send('hello, fucking world!'.encode('utf-8'))

data = sock.recv(1024)
sock.close()

print(data.decode('utf-8'))
