########## CODE2040 Registration #############
# POST request
# Erika A. Hairston 11/1/16

import sys
import re
import requests
import json
from pprint import pprint
import yaml
import datetime





######Receiving Enpoints#######
#####Step 1#####
endpoint1 = "http://challenge.code2040.org/api/register"


####Step 2#####
endpoint2 = "http://challenge.code2040.org/api/reverse"
endpoint2_5 = "http://challenge.code2040.org/api/reverse/validate"


#####Step 3#######
endpoint3 = "http://challenge.code2040.org/api/haystack"

#given a needle and a haystck, return index of needle or -1 if not found
def findInx(needle, haystack):
	index = 0
	for strg in haystack:
		if strg == needle:
			print("found index:")
			print(index)
			return index
		else:
 			index = index +1
 	return -1

#####Step 4#######
endpoint4 = "http://challenge.code2040.org/api/prefix"
def findPrefix(prx, collection, array):
	for strg in collection:
		if strg.startswith(prx):
			print("found index:")
		else:
			array.append(strg)
			print(strg)
 	return array
#####Step 5#######
endpoint5 = "http://challenge.code2040.org/api/dating"



############################################################



#####conent sent to endoint########
headers = {'Content-Type' : 'application/json'}
body = json.dumps({'token': '60003627513e0d6ab250539770e1d9ed', 'github': 'http://github.com/erikahairston/code2040Challenge'})

response = requests.post(endpoint5, data=body, headers = headers)
# Make the POST request here, passing body as the data:
print(response.status_code)
print(response.content)

##Step 2_5 post#####
# reversedS = response.content[::-1]
# body2 = json.dumps({'token': '60003627513e0d6ab250539770e1d9ed', 'string': reversedS})

# final = requests.post(endpoint2_5, data=body2, headers = headers)

# print(final.content)

# print("reverse")
# print(response.status_code)

# print(response.content[::-1])


######Step 3 post#####
# diction = json.loads(response.content)
# needle = diction.values()[1]
# haystack = diction.values()[0]


# print("dictionary")
# pprint(diction)

# print("neeedle")
# pprint(needle)

# print("haystack")
# pprint(haystack)
#index = findInx(needle,haystack)


# #####send results #####
# endpoint3_5 ="http://challenge.code2040.org/api/haystack/validate"
# body3 = json.dumps({'token': '60003627513e0d6ab250539770e1d9ed', 'needle': index})
# response3 = requests.post(endpoint3_5, data=body3, headers = headers)


# print(response3.status_code)
# print(response3.content)

#####Step 4 post######
# diction = yaml.safe_load(response.content)
# prefix = diction.values()[0]
# collect = diction.values()[1]
# print("dictionary")
# pprint(diction)

# print("prefix")
# pprint(prefix)

# print("colelction")
# pprint(collect)


# with_prx = []
# with_prx = findPrefix(prefix, collect, with_prx)

# print("final with prefix")
# print(with_prx)
# endpoint4 = "http://challenge.code2040.org/api/prefix/validate"
# body4 = json.dumps({'token': '60003627513e0d6ab250539770e1d9ed', 'array': with_prx})
# response4 = requests.post(endpoint4, data=body4, headers = headers)
# print(response4.status_code)
# print(response4.content)


#####Step 5 post######
diction = json.loads(response.content)
timestamp = datetime.datetime.strptime(diction.values()[0], "%Y-%m-%dT%H:%M:%SZ")
interval = diction.values()[1]

print("timestamp")
print(timestamp)

print("interval")
print(interval)
#T16:03:35Z

b = timestamp + datetime.timedelta(seconds=interval)

print b.isoformat()

b = b.isoformat() + 'Z'

endpoint5_1 = "http://challenge.code2040.org/api/dating/validate"
body5 = json.dumps({'token': '60003627513e0d6ab250539770e1d9ed', 'datestamp': b})
response5 = requests.post(endpoint5_1, data=body5, headers = headers)
print(response5.status_code)
print(response5.content)






