# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://rohit106bhushan.atlassian.net/rest/api/3/project"

API_TOKEN="ATATT3xFfGF0cy4DtYIxVxRIysCzmZV_YEEYqrnfUaspaimGnWLVhJ8iAGB5EbsWoGBF9REnU7p3t9dvWYlLWIrJK3tSiyLjYgCQnyD4h65vXWHArgLullt-Y77eLW1VI1qHf1Tc2aungw1XMaU6OCEQF3mMJEGf0kaYLUN3-asMKi4m2DbpK_4=8C2724AB"

auth = HTTPBasicAuth("rohit106bhushan@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output[0]["name"]

print(name)
