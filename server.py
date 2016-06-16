import socket
import atexit
from settings import *

def goodbye(conn):
    conn.close()

def setup_accept(sock):
    conn, addr = sock.accept()
    atexit.register(goodbye, conn)
    return conn

print "Sarting Static IP PI Python Server"
print "%s:%s" % (TCP_IP, TCP_PORT)

# Todo - Decent readme
# Todo - Setup Cron
# Todo - Try Excepts Around This Crap
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((TCP_IP, TCP_PORT))
sock.listen(1)

conn = setup_accept(sock)

while True:
    address = conn.recv(BUFFER_SIZE)
    print address
    conn.close()
    conn = setup_accept(sock)
    if FILE_PATH:
        if FILE_PATH[-1] == "/":
            filename = FILE_PATH + FILE_NAME
        else:
            filename = FILE_PATH + "/" + FILE_NAME
    else:
        filename = FILE_NAME

    f = open(filename, 'w')
    f.write(address)
    f.close()
