#!/usr/bin/python3

import sys


with open(sys.argv[1]) as fp:
    data = fp.read()

# Poor man's XML parser, but I didn't want any deps
t0 = data.split('<Key>')
t1 = [i.split('</Key>') for i in t0]
t2 = [i for s in t1 for i in s if i.startswith('builds/centos-8')][0]

print(t2)
