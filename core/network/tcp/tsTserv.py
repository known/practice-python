from socket import *
from time import ctime

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('等待客户端连接......')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...连接来源：', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send(bytes('[%s] %s' % (ctime(), data), 'utf-8'))

    tcpCliSock.close()
tcpSerSock.close()
