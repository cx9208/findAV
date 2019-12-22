# -*- coding: utf-8-*-
#!/usr/bin/python3
# by cx9208
import sys
import json
from colorama import init

init(autoreset=True)
print('')

if len(sys.argv) != 2:
    print('usage: findAV.py <tasklist.txt>')
    exit()
    
with open('avlist.json', 'rb') as f: # list by Uknow: github.com/uknowsec/get_AV/blob/master/av.json
    avlist=json.loads(f.read())
with open(sys.argv[1], 'rb') as f:
    tasklist=f.read().lower()

flag = False
for psname in avlist.keys():
    if tasklist.find(('\n'+psname).encode('utf-8').lower()) != -1:
        print('\033[0;31;40m\tFind\033[0m',psname,":",avlist[psname])
        flag = True

if not flag:
    print('Nothing found')
