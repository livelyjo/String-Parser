# Guide for Comma-Separated String Parser
This microservice will allow a user to send a string of values that are sepeated by commas and receive a JSON where keys will start with Ingredient 1: and increment up for every value.

Example:
- Input: "pepper, apples, pear"
- Output: {"Ingredient 1": "pepper", "Ingredient 2": "apples", "Ingredient 3": "pear"}
  
Any string can be sent to this microservice and the microservice will always respond with a JSON output. However, if your list is not seperated with commas then the output might not be what you expect.
## Server
This microservice is hosted by Rendar at this address https://string-parser-3.onrender.com. The server is using the free tier and will timeout periodically due to inactivity. If you aren't getting a response, wait at least 50 seconds and try again.
## Making Requests
This microservice only accepts HTTP GET reqeusts.

Example: 'https://string-parser-3.onrendar.com/ingredients?ingredients=apple, cherry, banana'

Formatting: '.../ingredients?ingredients={list}

List: A comma-seperated string

Code example:
```
import requests
ingredients = "apples,berries,pie"
json = requests.get('https://string-parser-3.onrender.com/ingredients', params={'ingredients': ingredients})
```
## Response
If a valid HTTP GET request is received the server will respond with a JSON formatted string. 

Example: 

- Request: 'https://string-parser-3.onrendar.com/ingredients?ingredients= apple, cherry, banana'
- Response: {'Ingredient 1': 'apple', 'Ingredient 2': 'cherry', 'Ingredient 3': 'banana'}
Code example:
```
import requests
ingredients = "apples,berries,pie"
json = requests.get('https://string-parser-3.onrender.com/ingredients', params={'ingredients': ingredients})
if json.status_code == 200:
    json_response = json.json()
    print(json_response)
```
## Sequence Diagram
![Screenshot 2024-08-05 111414](https://github.com/user-attachments/assets/fd49442c-49eb-4a58-81aa-7052019e0d8f)
