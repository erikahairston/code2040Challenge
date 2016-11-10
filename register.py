########## Example request #############
# POST /learn-http HTTP/1.1
# Host: www.codecademy.com
# Content-Type: text/html; charset=UTF-8
# Name=Eric&Age=26

import requests

body = {'token': '60003627513e0d6ab250539770e1d9ed', 'github': 'https://github.com/erikahairston/code2040Challenge'}

response = requests.post("http://challenge.code2040.org/api/register", data=body)
# Make the POST request here, passing body as the data:
