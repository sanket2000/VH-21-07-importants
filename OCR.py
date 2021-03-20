import requests
import base64
import json

with open("page0.jpg", "rb") as file:
    url = "https://api.imgbb.com/1/upload"
    payload = {
        "key": "052ec1db1544fb4209ef13e950a70970",
        "image": base64.b64encode(file.read()),
    }
    res = requests.post(url, payload)

if res.status_code == 200:
    #text = json(res)
    data  = res.json()
    imageurl = data['data']['url']
else:
    print("ERROR")
    print("Server Response: " + str(res.status_code))


url = "https://ocrly-image-to-text.p.rapidapi.com/"

querystring = {"imageurl": imageurl ,"filename":"sample.jpg"}

headers = {
    'x-rapidapi-key': "6fa3109806msh46d6751e3a8447ep128a96jsn3c693dd52315",
    'x-rapidapi-host': "ocrly-image-to-text.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

f = open("test.txt", "w")
f.write(response.text)
print("Text File generated")
