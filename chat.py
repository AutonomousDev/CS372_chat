import socket
from pynput.keyboard import Key, Listener
import os
import sys

class InvalidRole(Exception):
    print("Invalid Role. Enter -c or -s to select server or client role")
    pass


class Chat:

    def __init__(self, role, host="127.0.0.1", port=65432):
        self.role = role
        self.host = host  # Standard loopback interface address (localhost). Make "" to accept all connections.
        self.port = port  # Port to listen on (non-privileged ports are > 1023)"
        self.level = "                                                                     " + os.linesep +\
                     "                                                                     " + os.linesep +\
                     "                                                                     " + os.linesep +\
                     "                                                                     " + os.linesep +\
                     "====================================================================="

        if self.role == "-s":
            self.server()
        elif self.role == "-c":
            self.client()
        else:
            raise InvalidRole



    def get_host(self):
        return self.host

    def get_port(self):
        return self.port

    def get_level(self):
        return self.level

    def clear_console(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

    def server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((self.get_host(), self.get_port()))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    self.clear_console()
                    for i in self.get_level():
                        print(i)
                    data = conn.recv(1024)

                    data = bytes(self.get_level(), "utf-8")
                    conn.sendall(data)

    def client(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.get_host(), self.get_port()))

            while True:
                self.clear_console()
                data = "some text"
                data = bytes(data, 'utf-8')
                s.sendall(data)
                data = s.recv(1024)
                print(f"Received {data!r}")

