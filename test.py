import requests

ingredients = "apples,berries,pie"
json = requests.get('http://127.0.0.1:5000/ingredients', params={'ingredients': ingredients})

if json.status_code == 200:
    json_response = json.json()
    print(json_response)

ingredients = "apples, berries, pie"
json = requests.get('http://127.0.0.1:5000/ingredients', params={'ingredients': ingredients})

if json.status_code == 200:
    json_response = json.json()
    print(json_response)

ingredients = "      apples , berries     , pie                                  "
json = requests.get('http://127.0.0.1:5000/ingredients', params={'ingredients': ingredients})

if json.status_code == 200:
    json_response = json.json()
    print(json_response)

ingredients = " apples, berries , pie, sourdough, pepper,  lemon pepper, artichoke"
json = requests.get('http://127.0.0.1:5000/ingredients', params={'ingredients': ingredients})

if json.status_code == 200:
    json_response = json.json()
    print(json_response)

json = requests.get('http://127.0.0.1:5000/ingredients?ingredients= apples, lemons, pears')

if json.status_code == 200:
    json_response = json.json()
    print(json_response)
