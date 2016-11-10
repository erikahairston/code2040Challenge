########## CODE2040 Registration #############
# POST request
# Erika A. Hairston 11/1/16

import sys
import re
import requests
import json
from pprint import pprint


######Receiving Enpoints#######
#####Step 1#####
endpoint1 = "http://challenge.code2040.org/api/register"


####Step 2#####
endpoint2 = "http://challenge.code2040.org/api/reverse"
endpoint2_5 = "http://challenge.code2040.org/api/reverse/validate"


#####Step 3#######
endpoint3 = "http://challenge.code2040.org/api/haystack"

############################################################



#####conent sent to endoint########
headers = {'Content-Type' : 'application/json'}
body = json.dumps({'token': '60003627513e0d6ab250539770e1d9ed', 'github': 'http://github.com/erikahairston/code2040Challenge'})

response = requests.post(endpoint3, data=body, headers = headers)
# Make the POST request here, passing body as the data:
print(response.status_code)


##Step 2_5 post#####
# reversedS = response.content[::-1]
# body2 = json.dumps({'token': '60003627513e0d6ab250539770e1d9ed', 'string': reversedS})

# final = requests.post(endpoint2_5, data=body2, headers = headers)

# print(final.content)

# print("reverse")
# print(response.status_code)

# print(response.content[::-1])


##Step 3 post#####
diction = json.loads(response.content)
needle = diction.values()[1]
haystack = diction.values()[0]


print("dictionary")
pprint(diction)

print("neeedle")
pprint(needle)

print("haystack")
pprint(haystack)

index = 0

for strg in haystack:
	if strg == needle:
		print("found index:")
		print(index)
		exit()
	else:
		index = index +1
print("needle not found")



