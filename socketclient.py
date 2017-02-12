#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 01:21:57 2017

@author: nick
"""

import socket

s = socket.socket()
host = '50.131.6.174'
port = 2424
s.connect((host, port))
print s.recv(1024)
inpt = raw_input('type anything and click enter... ')
s.send(inpt)
print "the message has been sent"