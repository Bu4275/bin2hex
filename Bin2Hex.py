#!/usr/bin/python
#coding:utf-8
import sys
path = sys.argv[0]

line = 20
f = open(path,"rb")

print 'char shellcode[]='
sys.stdout.write('\"')
for b in f.read():
    sys.stdout.write(r'\x{:02x}'.format(ord(b)))
    line -= 1
    if line == 0:
        print '\"'
        sys.stdout.write(r'"')
        line = 20


sys.stdout.write('\"');
f.close()
