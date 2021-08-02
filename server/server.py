from filter.filter import FilterBadWords
import socket


class Server:
    def __init__(self):
        sock = socket.socket()
        sock.bind(('', 9090))
        sock.listen(1)
        self.conn, addr = sock.accept()

    def recive(self):
        while True:
            data = self.conn.recv(1024)
            if not data:
                break
            self.conn.send(data.upper())
            print(data.decode('utf-8'))
        self.conn.close()

if __name__ == '__main__':
    my_server = Server()
    my_server.recive()
