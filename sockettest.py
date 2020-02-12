#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 01:21:26 2017

@author: nick
"""

BLOCK_SIZE = 8096
COMMAND_SIZE = 64


import socket, sys, os, time

def command_str(command, fn, size):
    command_string = command + ' ' + fn + ' ' + str(size) + ' '
    command_string += '0' * (COMMAND_SIZE - len(command_string)) # fill remainder of command string with 0s
    return command_string
    
def parse_command_str(command_str):
    command, fn, size, pad = command_str.split(' ')
    return command, fn, int(size)
    
    

        

class ImageHostClient:

    def __init__(self):
        self.s = socket.socket()
        self.s.connect(("localhost",2424))
        
    def send_file(self, fn):
        size = os.path.getsize(fn) # TODO: write this so that if file changes it doesnt cause problems
        self.s.send(command_str("SENDFILE", fn, size))
        f = open(fn, "rb")
        remaining = size
        while remaining > 0:
            l = f.read(BLOCK_SIZE)
            remaining -= BLOCK_SIZE
            self.s.send(l)
        f.close()
        
    def get_file(self, fn):
        self.s.send(command_str("GETFILE", fn, 0))
        ack = self.s.recv(COMMAND_SIZE)
        command, fn, size = parse_command_str(ack)
        f = open(fn, "wb")
        remaining = size
        while remaining > BLOCK_SIZE:
            l = self.s.recv(BLOCK_SIZE)
            f.write(l)
            remaining -= BLOCK_SIZE
        l = self.s.recv(remaining)
        f.write(l)
        f.close()
        
    def close(self):
        self.s.close()
    
class ImageHostServer:
    
    def __init__(self):
        self.s = socket.socket()
        self.s.bind(("localhost",2424))
        self.s.listen(5)
        self.connect()
        self.wait_command()
        
    def connect(self):
        self.sc, self.address = self.s.accept()
        
    def wait_command(self):
        while True:
            command_string = self.sc.recv(COMMAND_SIZE)
            if len(command_string) == 0: # must have been disconnected
                self.connect()
                continue
            # not disconnected, so execute command
            command, fn, size = parse_command_str(command_string)
            if command == 'SENDFILE':
                self.receive_file(fn, size)
            elif command == 'GETFILE':
                self.send_file(fn)
            else:
                print 'Unrecognized Command'
        
    def receive_file(self, fn, size):
        print 'receiving file'
        f = open('images/' + fn, 'wb')
        remaining = size
        while remaining > BLOCK_SIZE:       
            l = self.sc.recv(BLOCK_SIZE)
            f.write(l)
            remaining -= BLOCK_SIZE
        l = self.sc.recv(remaining)
        f.write(l)
        f.close()
        #self.sc.close()
        print 'done'
        
    def send_file(self, fn):
        print 'sending file'
        size = os.path.getsize('images/' + fn) # TODO: write this so that if file changes it doesnt cause problems
        self.sc.send(command_str("GETFILE", fn, size))
        f = open('images/' + fn, 'rb')
        remaining = size
        while remaining > 0:
            l = f.read(BLOCK_SIZE)
            self.sc.send(l)
            remaining -= BLOCK_SIZE
        f.close()
        #self.sc.close()
        print 'done'
        
    def close(self):
        #self.sc.close()
        self.s.close()
        
    
if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit()
        
    args = sys.argv[1:]
    if args[0] == '-s':
        ImageHostServer()
    elif args[0] == '-c':
        ImageHostClient()






    
