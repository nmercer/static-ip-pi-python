import socket
from settings import *

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(PASSWORD, (UDP_IP, UDP_PORT))
