import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/pszemraj/flan-t5-large-grammar-synthesis"
headers = {"Authorization": "Bearer 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"}


@app.route('/query', methods=['GET', 'POST'])
def query():
    input_text = None
    output = None
    if request.method == "POST":
        input_text = request.form["input_text"]
        # T5 모델 API 호출
        response = requests.post(API_URL, headers=headers, json={"inputs": input_text})
        output = response.json()[0]["generated_text"]
    return render_template("index.html", input_text=input_text, output=output)

if __name__ == '__main__':
    app.run(debug=True)