# -*- coding: utf-8 -*-
import socket
import threading_demo


def handler(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    # 有新的连接来了就向客户端发送一条记录表示欢迎
    sock.send('Welcome!')
    # 接受客户端发来的消息
    b = []
    while True:
        data = sock.recv(1024)
        if data:
            b.append(data)
        else:
            break
    data_str = ''.join(b)
    print 'Receive from client data : %s ' % data_str
    sock.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8888))
server.listen(5)
print 'Waiting for connection ...'
while True:
    # 接受一个新连接
    sock, addr = server.accept()
    # 创建新线程来处理
    t = threading_demo.Thread(target=handler, args=(sock, addr))
    t.start()