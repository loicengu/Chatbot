import json
import random
from flask import Flask, jsonify, render_template

app = Flask(__name__)

def load_vocabularies_from_json(json_file):
    with open(json_file, "r") as file:
        return json.load(file)

def get_new_word(vocabularies):
    word = random.choice(list(vocabularies.keys()))
    definition = vocabularies[word]["definition"]
    return word, definition

# Load vocabularies from the JSON file
vocabularies_file = "vocabularies.json"
vocabularies = load_vocabularies_from_json(vocabularies_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_word')
def get_word():
    word, definition = get_new_word(vocabularies)
    return jsonify({"word": word, "definition": definition})

if __name__ == '__main__':
    app.run(debug=True)
