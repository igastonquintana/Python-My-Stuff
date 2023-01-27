import socket

s = socket.socket()


s.bind(("localhost", 12345))
s.listen(5)

clients = []
while True:
    c, addr = s.accept()
    clients.append(c)

    while True:
        message = input("You: ")
        for client in clients:
            client.send(message.encode())

c.close()

