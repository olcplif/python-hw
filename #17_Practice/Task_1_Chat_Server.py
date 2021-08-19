import socket
import re

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 5050))
clients = {}
print("Server start")
while True:
    data, address = sock.recvfrom(1024)
    recipient_nickname = re.search("@(.*),", data.decode('utf-8'))
    print(address)
    username_is_used = False
    if recipient_nickname is None:
        if address not in clients.keys():
            for client in clients.keys():
                if re.search("\[(.*)\]", data.decode('utf-8')).group(0) == clients[client]:
                    username_is_used = True
                    sock.sendto("username_error".encode('utf-8'), address)
                    break

            if username_is_used:
                continue
            sock.sendto("Welcome to chat!".encode('utf-8'), address)
        clients[address] = re.search("\[(.*)\]", data.decode('utf-8')).group(0)

        for client in clients:
            if client == address:
                continue
            sock.sendto(data, client)
    else:
        recipient_nickname = recipient_nickname.group(0)
        recipient_nickname = list(recipient_nickname)
        del recipient_nickname[0]
        del recipient_nickname[-1]
        recipient_nickname = "".join(recipient_nickname)
        for address in clients:
            if clients[address] == "[" + recipient_nickname + "]":
                sock.sendto(data, address)
