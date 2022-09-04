import socket

server = socket.socket()
print("Socket Created")

server.bind(('localhost',9898))
print("Socket binded woth port")

server.listen(5)
print("wait for connect")

client,port = server.accept()

while True:
    msg=client.recv(1024).decode()
    print("client:",msg)
    inp = input("server:")
    client.send(bytes(inp,'utf-8'))
