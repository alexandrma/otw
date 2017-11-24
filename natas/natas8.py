#!/usr/bin/env python
import binascii
import base64

import requests
#http://docs.python-requests.org/en/master/
#payload={'page':'home'}
eS="3d3d516343746d4d6d6c315669563362"
eSs=base64.standard_b64decode(binascii.unhexlify(eS)[::-1])
payload={'submit':'submit','secret':eSs}

url="http://natas8.natas.labs.overthewire.org"
r=requests.post(url, data=payload, auth=('natas8','DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'))

#print base64.standard_b64decode(binascii.unhexlify(eS)[::-1])
print eSs

print r.text
