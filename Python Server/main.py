import socket
import threading

#IPv4
#TCP Connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Port = 10000
sock.bind(('0.0.0.0', 10000))

#Number of pending connections = 1
sock.listen(1)

connections = []

def handler(c, a):
    global connections
    while True:
        #Recieves maximum 1024 Bytes
        data = c.recv(1024)
        for connection in connections:
            connection.send(bytes(data))
            if not data:
                connections.remove(c)
                c.close()
                break

while True:
    #c = connection
    #a = clients IP-Address
    c, a = sock.accept()
    cThread = threading.Thread(target=handler, args=(c,a))
    cThread.daemon = True
    cThread.start()
    connections.append(c)
    print(connections)
