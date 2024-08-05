from flask import Flask, request
import json


app = Flask(__name__)


@app.route('/ingredients')
def ingredients():
    ingredients = request.args.get('ingredients')
    ingredient = ''
    dictionary = {}
    count = 1
    for character in ingredients:
        if character != ',':
            ingredient += character
        else:
            dictionary[f'Ingredient {count}'] = ingredient.strip()
            ingredient = ''
            count += 1
    dictionary[f'Ingredient {count}'] = ingredient.strip()
    json_dictionary = json.dumps(dictionary)
    print(json_dictionary)
    return json_dictionary


if __name__=='__main__':
    app.run()