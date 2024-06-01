#!workspace/bin/python

import requests
import json 

# pull data
OBJECT = requests.get("https://api.github.com/users/khikmatillo1") 

# if site is working
if OBJECT.status_code ==200:
    # convert data to json
    content = json.loads(OBJECT.text)
    # print to screen
    print(content["company"])
