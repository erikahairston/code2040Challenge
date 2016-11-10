########## CODE2040 Registration #############
# POST request
# Erika A. Hairston 11/1/16

import sys
import re
import requests
import json

headers = {'Content-Type' : 'application/json'}
body = json.dumps({'token': '60003627513e0d6ab250539770e1d9ed', 'github': 'http://github.com/erikahairston/code2040Challenge'})

response = requests.post("http://challenge.code2040.org/api/register", data=body, headers = headers)
# Make the POST request here, passing body as the data:

print(response.status_code)
print(response.content)
