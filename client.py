import socket
from settings import *
import ipgetter

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))
sock.send(ipgetter.myip())
data = sock.recv(BUFFER_SIZE)
sock.close()
