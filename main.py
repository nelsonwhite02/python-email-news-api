import requests
from sent_email import send_email

topic = "tesla"
api_key = "0e8d5e7d4343436ab510defb2a1b2487"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-07-01&" \
      "sortBy=publishedAt&" \
      "apiKey=0e8d5e7d4343436ab510defb2a1b2487&language=en"

#  make a request
request = requests.get(url)

#  Get a dictionary with data
content = request.json()

#  access articles with descriptions and title
body =""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" + "\n" + body + article["title"] + "\n" \
               + article["description"] \
               + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)