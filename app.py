from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('input.html')

@app.route('/save-json', methods=['POST'])
def save_json():
    data = request.json
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)
    return 'Data saved successfully'

if __name__ == '__main__':
    app.run(debug=True)
