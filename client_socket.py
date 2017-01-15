# -*- coding: utf-8 -*-
import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8888))
# 接受服务器返回的消息
print client.recv(1024)
# 向服务起发送一条消息
client.send('I am a client ...')



