import requests

api_key = "0e8d5e7d4343436ab510defb2a1b2487"
url = "https://newsapi.org/v2/everything?q=tesla&from=" \
       "2023-07-01&sortBy=publishedAt&apiKey=" \
       "0e8d5e7d4343436ab510defb2a1b2487"

#  make a request
request = requests.get(url)

#  Get a dictionary with data
content = request.json()

#  access articles with descriptions and title
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
