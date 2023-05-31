from flask import Flask, render_template, request, jsonify
import json
import random
import os

app = Flask(__name__)

# Определите путь к файлу data.json
json_path = ""

def read_json_file():
    with open(json_path, 'r') as json_file:
        data = json.load(json_file)
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_random_value')
def getRandomValue(data):
    randomValue = {}
    for key in data[0]:
        if key:
            column = [item[key] for item in data]
            randomValue[key] = random.choice(column)
    return randomValue

@app.route('/upload_json', methods=['POST'])
def upload_json():
    global json_path
    file = request.files['file']
    if file:
        filename = file.filename
        file.save(os.path.join(app.root_path, filename))
        json_path = os.path.join(app.root_path, filename)
    return jsonify({'message': 'File uploaded successfully.'})

if __name__ == '__main__':
    app.run()
