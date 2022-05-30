# echo-server.py
import socket

def server():
    HOST = "127.0.0.1"  # Standard loopback interface address (localhost). Make "" to accept all connections.
    PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
    # username = input("Username? ")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                # decode and print
                data = conn.recv(1024)
                data = data.decode("utf-8")
                if data == "/q":
                    data = bytes(data, 'utf-8')
                    conn.sendall(data)
                    conn.close()
                    return print("Disconnected")
                print(data)

                # Reply
                # prompt = username + ": "
                # data = input(prompt)
                # data = username + ": " + data
                data = input()
                data = bytes(data, 'utf-8')
                conn.sendall(data)


server()