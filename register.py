########## CODE2040 Registration #############
# POST request
# Erika A. Hairston 11/1/16

import sys
import re
import requests
import json


#####Step 1#####
endpoint1 = "http://challenge.code2040.org/api/register"


####Step 2#####
endpoint2 = "http://challenge.code2040.org/api/reverse"
endpoint2_5 = "http://challenge.code2040.org/api/reverse/validate"

headers = {'Content-Type' : 'application/json'}
body = json.dumps({'token': '60003627513e0d6ab250539770e1d9ed', 'github': 'http://github.com/erikahairston/code2040Challenge'})

response = requests.post(endpoint2, data=body, headers = headers)
# Make the POST request here, passing body as the data:

print(response.status_code)
print(response.content)

print("reverse")

##Step 2_5 post#####
reversedS = response.content[::-1]
body2 = json.dumps({'token': '60003627513e0d6ab250539770e1d9ed', 'string': reversedS})

final = requests.post(endpoint2_5, data=body2, headers = headers)

print(final.content)

print("reverse")
print(response.status_code)
print(response.content[::-1])






