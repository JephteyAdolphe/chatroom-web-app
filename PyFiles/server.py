import socket

HEADEERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!!")

    msg = "Welcome to the server!"
    msg = f"{len(msg):<{HEADEERSIZE}}" + msg

    clientsocket.send(bytes(msg, "utf-8"))
