from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = 'localhost'
PORT = 21567
ADDR = (HOST, PORT)


class MyRequestHandler(SRH):
    def handle(self):
        print('...连接来源：', self.client_address)
        self.wfile.write(bytes('[%s] %s' %
                               (ctime(), self.rfile.readline()), 'utf-8'))


tcpServ = TCP(ADDR, MyRequestHandler)
print('等待客户端连接......')
tcpServ.serve_forever()
