# Name: Cameron Bowers
# OSU Email: bowercam@oregonstate.edu
# Course: CS372 - Intro To Networking
# Assignment: RDT
# Due Date: 6/04/2022
# Description: This program is a simple chat program
# Cited sources: https://docs.python.org/3/howto/sockets.html

import socket


def client():
    """The client half of the chat"""
    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 65432  # The port used by the server

    # Connect to server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        while True:
            # send reply
            data = input()
            data = bytes(data, 'utf-8')
            s.sendall(data)

            # Receive reply
            data = s.recv(1024)
            data = data.decode("utf-8")

            # Detect disconnect
            if data == "/q":
                data = bytes(data, 'utf-8')
                s.sendall(data)     # Disconnect the client
                s.close()           # Disconnect the self
                return print("Disconnected")
            print(data)


client()
