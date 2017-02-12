#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 01:21:57 2017

@author: nick
"""

import socket
import sys

s = socket.socket()
s.connect(("localhost",2424))
f = open ("test.jpg", "rb")
l = f.read(1024)
while (l):
    s.send(l)
    l = f.read(8096)
s.close()