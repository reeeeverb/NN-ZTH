import requests
x = requests.get('https://api.urbandictionary.com/v0/define?term=lit')
out = x.text
print(x.text[x.text.index("\"example\":"):x.text.index("\"thumbs_down\":")])

