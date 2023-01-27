import socket

s = socket.socket()

s.connect(("localhost", 12345))

while True:
    data = s.recv(1024).decode()
    print("Server: " + data)
    message = input("You: ")
    s.send(message.encode())

s.close()

