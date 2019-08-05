#!/usr/bin/python3
#客户端 client

from socket import *

host=''
port=0

if host=='':
    host=input('请输入主机名称或IP:')
    print('[Host]%s' % host)
if port==0:
    port=int(input('请输入服务器端口号(1025-65535):'))
    if port<1025 or port>65535:
        print('[Error]输入错误！')
        exit()
    print('[Port]%d' % port)

maxbyte=1024
serveraddr=(host,port)

serversocket=socket(AF_INET,SOCK_STREAM)

serversocket.connect(serveraddr)
while True:
    msg=input('>')
    serversocket.send(msg.encode('utf-8'))
    if msg!='':
        msg=serversocket.recv(maxbyte)
        print('[Message] %s' % msg.decode('utf-8'))
    if msg=='' or msg==b'!@exit':
        serversocket.close()
        break
