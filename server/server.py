import socket
from filter.filter import FilterBadWords
from flask import Flask

app = Flask(__name__)


class Server:
    def __init__(self, host, port):
        self.my_filter = FilterBadWords('../filter/resources/list_of_bad_words.txt')
        sock = socket.socket()
        sock.bind((host, port))
        sock.listen(1)
        self.conn, addr = sock.accept()

    def recive(self):
        data = self.conn.recv(1024)
        self.conn.send(data.upper())
        self.conn.close()
        return self.my_filter.filter(data.decode('utf-8'))


@app.route("/")
def start_server():
    my_server = Server('', 9080)
    return my_server.recive()


if __name__ == "__main__":
    app.run()

