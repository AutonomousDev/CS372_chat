# Name: Cameron Bowers
# OSU Email: bowercam@oregonstate.edu
# Course: CS372 - Intro To Networking
# Assignment: RDT
# Due Date: 6/04/2022
# Description: This program is a simple chat program
# Cited sources: https://docs.python.org/3/howto/sockets.html

import socket

def server():
    """The server host this connection with the client"""
    HOST = "127.0.0.1"  # Standard loopback interface address (localhost). Make "" to accept all connections.
    PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

    # Initialize the socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                # Receive reply
                data = conn.recv(1024)
                data = data.decode("utf-8")

                # Detect disconnect
                if data == "/q":
                    data = bytes(data, 'utf-8')
                    conn.sendall(data)  # Disconnect the client
                    conn.close()        # Disconnect the self
                    return print("Disconnected")
                print(data)

                # Send Reply
                data = input()
                data = bytes(data, 'utf-8')
                conn.sendall(data)


server()
