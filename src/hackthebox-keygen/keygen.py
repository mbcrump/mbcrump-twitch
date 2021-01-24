#!/usr/bin/env python3
# create a code to use with
# hackthebox.eu

import requests
import base64

url = 'https://www.hackthebox.eu/api/invite/generate'
headers = {'content-type': 'application/json', 'user-agent': 'I bet you wish you knew'}
x = requests.post(url, headers=headers)
data = x.json()
value = data['data']['code']

base = base64.b64decode(value)

print ("Your hackthebox invite code is : " + base.decode('utf-8'))
