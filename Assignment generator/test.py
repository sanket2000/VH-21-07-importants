import requests

url = "https://ocrly-image-to-text.p.rapidapi.com/"

querystring = {"imageurl":"https://4ww1y37tl91gmoej12r01u1c-wpengine.netdna-ssl.com/wp-content/uploads/2019/08/TextDocument.png","filename":"sample.jpg"}

headers = {
    'x-rapidapi-key': "6fa3109806msh46d6751e3a8447ep128a96jsn3c693dd52315",
    'x-rapidapi-host': "ocrly-image-to-text.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

f = open("test.txt", "w")
f.write(response.text)
