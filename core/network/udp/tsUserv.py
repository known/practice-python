from socket import *
from time import ctime

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('等待客户端连接......')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto(bytes('[%s] %s' % (ctime, data), 'utf-8'), addr)
    print('...连接来源：', addr)

udpSerSock.close()
