#!/usr/bin/python3
#服务端 server

from socket import *

host=''
port=0

if port==0:
    port=int(input('请输入开放端口号(1025-65535):'))
    if port<1025 or port>65535:
        print('[Error] 输入错误！')
        exit()
    print('[Port] %d' % port)

maxbyte=1024
serveraddr=(host,port)

serversocket=socket(AF_INET,SOCK_STREAM)
serversocket.bind(serveraddr)
serversocket.listen(5)

while True:
    clientsocket,clientaddr=serversocket.accept()
    print('[Waring] 连接地址:%s' % str(clientaddr))
    while True:
        msg=clientsocket.recv(maxbyte)
        clientsocket.send(msg)
        if not msg:
            clientsocket.close()
            break
        elif msg==b'!@exit':
            clientsocket.close()
            serversocket.close()
            exit()
        print('[Message] %s' % msg.decode('utf-8'))
