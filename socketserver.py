#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 01:21:26 2017

@author: nick
"""

import socket
import sys
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
    
