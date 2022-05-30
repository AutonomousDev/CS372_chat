def client():
    import socket

    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 65432  # The port used by the server
    username = input("Username? ")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        while True:
            data = input()
            data = bytes(data, 'utf-8')
            s.sendall(data)
            data = s.recv(1024)
            print(f"Received {data!r}")

client()