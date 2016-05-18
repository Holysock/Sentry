import socket


TCP_IP = '172.0.0.1'
TCP_PORT = 1234
BUFFER_SIZE = 1024 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_Port))






s.close()


