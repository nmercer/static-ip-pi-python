import socket
from settings import *

print "Sarting Static IP PI Python Server"
print "%s:%s" % (UDP_IP, UDP_PORT)

# Todo - Decent readme
# Todo - Setup Cron
# Todo - Try Excepts Around This Crap
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    password, addr = sock.recvfrom(1024)
    if password == PASSWORD:
        if FILE_PATH:
            if FILE_PATH[-1] == "/":
                filename = FILE_PATH + FILE_NAME
            else:
                filename = FILE_PATH + "/" + FILE_NAME
        else:
            filename = FILE_NAME

        f = open(filename, 'w')
        f.write(addr[0])
        f.close()
