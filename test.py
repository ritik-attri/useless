#example to get response using python

import requests 
  
URL = "http://localhost/certificate/email"
r = requests.get(URL) 

with open(r'path\certificate.pdf','wb') as f:
    f.write(r.content)