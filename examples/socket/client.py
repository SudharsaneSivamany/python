import socket

client = socket.socket()

client.connect(('localhost',9898))

while True:
    inp = input("client:") 
    client.send(bytes(inp,'utf-8'))
    msg = client.recv(1024).decode()
    print("server:",msg)
    

