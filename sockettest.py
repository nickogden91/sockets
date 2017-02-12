#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 01:21:26 2017

@author: nick
"""

import socket, sys

class SocketTest:
    
    def __init__(self):
       pass

class SocketTestClient:

    def __init__(self):
        s = socket.socket()
        s.connect(("localhost",2424))
        f = open ("test.jpg", "rb")
        l = f.read(1024)
        while (l):
            s.send(l)
            l = f.read(8096)
        s.close()
    
class SocketTestServer:
    
    def __init__(self):
        s = socket.socket()
        s.bind(("localhost",2424))
        s.listen(5)
        while True:
            sc, address = s.accept()
            print address
            f = open('images/test.jpg','wb') #open in binary
            while (True):       
                l = sc.recv(8096)
                while (l):
                        f.write(l)
                        l = sc.recv(8096)
            f.close()
            sc.close()
        s.close()
    
if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit()
        
    args = sys.argv[1:]
    if args[0] == '-s':
        SocketTestServer()
    elif args[0] == '-c':
        SocketTestClient()






    
