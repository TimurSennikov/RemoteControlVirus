import threading
import socket

from .socket_commands import *

class SockAnswer(threading.Thread):
    def __init__(self, c, sock_n):
        threading.Thread.__init__(self=self)
        self.name = "socket_ans" + str(sock_n)

        self.sock_n = sock_n

        self.connection = c
        self.running = True

    def run(self):
        self.connection.send(("HELLO №" + str(self.sock_n) + ", THIS IS SOCKET INTERFACE OF HLUPOVIRUS, HAVE FUN!" + '\n').encode())

        phrase = ""
        while self.running:
            phrase = self.connection.recv(1024).decode()
            self.connection.send("PROCESSING...\n".encode())

            if phrase == '\n':
                self.connection.send(("OK, LEAVING, BYE №" + str(self.sock_n) + '\n').encode())

                self.connection.close()
                self.running = False
                return False
            else:
                handle_socket_commands(self.connection, phrase)

class SockThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.name = "socket_thread"
        self.sock_n = 0

    def run(self):
        s = socket.socket()
        s.bind(('', 9969))
        s.listen(3)

        while True:
            c, addr = s.accept()

            print(addr)

            a = SockAnswer(c=c, sock_n=self.sock_n)
            self.sock_n += 1

            a.start()