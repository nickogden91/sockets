#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 01:21:26 2017

@author: nick
"""

import socket

s = socket.socket()
host = ''
port = 2424
s.bind((host,port))
s.listen(5)
while True:
    c, addr = s.accept()
    print("Connection accepted from " + repr(addr[1]))
    c.send("Server approved connection\n")
    print repr(addr[1]) + ": " + c.recv(1026)
    c.close()