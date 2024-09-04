# 客户端
import socket

# 1.创建socket对象
client_socket=socket.socket()

# 2.IP地址和端口，向服务端发送连接请求
ip='127.0.0.1'
port=8888
client_socket.connect((ip,port))
print('与服务器连接成功')

# 3.发送数据
client_socket.send('hello ninao do you eating'.encode('utf-8'))

# 4.关闭
client_socket.close()
print('发送完毕')