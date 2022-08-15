import requests
import json
import urllib.request
url = 'http://127.0.0.1:8000/api/'
response = urllib.request.urlopen(url)
data = json.loads(response.read())


last = data[-1]
location = last.get("id")

string_location = str(location)

withformat = string_location+"/"


url2 = 'http://127.0.0.1:8000/details/'+withformat

myobj = {"unique": "gotitbero"}


x = requests.put(url2, json = myobj)

print(x.text)