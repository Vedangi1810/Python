# Get PR info on a repo using python
# serach github api doc

import requests
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
details = response.json()

for i in range(len(details)):
    print(details[i]["user"]["login"], ": ", details[i]["number"])
    
