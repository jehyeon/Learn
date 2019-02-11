# FileName  : client.py
# Author    : Lee, Jehyeon

import socket

s = socket.socket()
host = socket.gethostname()
PORT = 7523

s.connect((host, PORT))
print('Conntected to ', host)

while True:
    msg = input("Enter something for the server: ")
    s.send(msg.encode('utf-8'))
    # Halts
    print('[Waiting for response...]')
    print((s.recv(1024)).decode('utf-8'))