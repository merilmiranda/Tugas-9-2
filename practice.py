import requests

api_key = "40bcbe4b-17be-4945-874f-768f27a33f7c"
word = "potato"
url = f"https://dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"

res =requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)