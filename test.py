import requests

ingredients = "apples,berries,pie"
json = requests.get('https://string-parser-3.onrender.com/ingredients', params={'ingredients': ingredients})

if json.status_code == 200:
    json_response = json.json()
    print(json_response)

ingredients = "apples, berries, pie"
json = requests.get('https://string-parser-3.onrender.com/ingredients', params={'ingredients': ingredients})

if json.status_code == 200:
    json_response = json.json()
    print(json_response)

ingredients = "      apples , berries     , pie                                  "
json = requests.get('https://string-parser-3.onrender.com/ingredients', params={'ingredients': ingredients})

if json.status_code == 200:
    json_response = json.json()
    print(json_response)

ingredients = " apples, berries , pie, sourdough, pepper,  lemon pepper, artichoke"
json = requests.get('https://string-parser-3.onrender.com/ingredients', params={'ingredients': ingredients})

if json.status_code == 200:
    json_response = json.json()
    print(json_response)

json = requests.get('https://string-parser-3.onrender.com/ingredients?ingredients= apples, pears, peaches')

if json.status_code == 200:
    json_response = json.json()
    print(json_response)
