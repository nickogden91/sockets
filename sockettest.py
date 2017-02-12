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
        self.s = socket.socket()
        self.s.connect(("localhost",2424))
        self.get_file('test.jpg')
        
    def send_file(self, fn):
        self.s.send("SEND FILE")
        f = open(fn, "rb")
        l = f.read(1024)
        while l:
            self.s.send(l)
            l = f.read(8096)
        f.close()
        self.s.close()
        
    def get_file(self, fn):
        self.s.send("GET FILE")
        f = open(fn, "wb")
        l = self.s.recv(8096)
        while l:
            f.write(l)
            l = self.s.recv(8096)
        f.close()
        self.s.close()
    
class SocketTestServer:
    
    def __init__(self):
        self.s = socket.socket()
        self.s.bind(("localhost",2424))
        self.s.listen(5)
        self.wait()
        
    def wait(self):
        while True:
            self.sc, self.address = self.s.accept()
            command = self.sc.recv(8096)
            print command
            if command == 'SEND FILE':
                self.receive_file('images/test.jpg')
            elif command == 'GET FILE':
                self.send_file('images/test.jpg')
            else:
                print 'Unrecognized Command'
        self.s.close()
        
    def receive_file(self, fn):
        f = open(fn,'wb')
        while (True):       
            l = self.sc.recv(8096)
            while (l):
                    f.write(l)
                    l = self.sc.recv(8096)
        f.close()
        self.sc.close()
        
    def send_file(self, fn):
        f = open(fn,'rb')
        while (True):    
            l = f.read(8096)
            while (l):
                self.sc.send(l)
                l = f.read(8096)
        f.close()
        self.sc.close()
        
    
if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit()
        
    args = sys.argv[1:]
    if args[0] == '-s':
        SocketTestServer()
    elif args[0] == '-c':
        SocketTestClient()






    
