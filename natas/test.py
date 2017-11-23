import requests
#http://docs.python-requests.org/en/master/
payload={'submit':'submit','secret':'FOEIUWGHFEEUHOFUOIU'}
url="http://natas6.natas.labs.overthewire.org"
authdata={'natas6','aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'}

r=requests.post(url, data=payload, auth=authdata)
#r=requests.post(url, data=payload, auth=('natas6','aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'))

print r.text
