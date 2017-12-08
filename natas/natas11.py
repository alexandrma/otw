#!/usr/bin/env python
#inspired by https://multiplex3r.github.io/posts/2016-09-25-over-the-wire-natas-11-15/
import base64
import requests
key = ''
plaintext = '{"showpassword":"no","bgcolor":"#ffffff"}'
for c1, c2 in zip(base64.b64decode('ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw='), plaintext):
#zip(*iterables) make an iterator that aggregates elements from each of the iterables.
	key += chr(ord(c1) ^ ord(c2))
#chr(i) return the string representing a character whose Unicode code point is the integer i.
#ord(i) given a string representing one Unicode character, return an integer representing the Unicode code point of that character. inverse of crh()
print key
key = 'qw8J'
#key is a sequence of 'qw8J'. It means others 'qw8J' we can throw out
ciphertext = ''
plaintext = '{"showpassword":"yes","bgcolor":"#ffffff"}'
#neet to change "showpassword":"no" to showpassword":"yes" 
for i in range(len(plaintext)): #in the end of loop important ":" 
	d=plaintext[i]
	ciphertext += chr(ord(d) ^ ord(key[i % len(key)]))
print base64.b64encode(ciphertext)

payload={'needle':'c /etc/natas_webpass/natas11 /#','submit':'Search'}
url="http://natas11.natas.labs.overthewire.org"
cookies = dict(data='ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK')
r=requests.post(url, cookies=cookies, auth=('natas11','U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'))
print r.text

