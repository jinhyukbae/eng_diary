import sqlite3
from datetime import datetime

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import nltk
from flask import Flask, render_template, request

# nltk.download('punkt')

tokenizer = AutoTokenizer.from_pretrained("fabiochiu/t5-base-tag-generation")
model = AutoModelForSeq2SeqLM.from_pretrained("fabiochiu/t5-base-tag-generation")

tag = Flask(__name__)

# 데이터베이스 연결 및 테이블 생성
conn = sqlite3.connect('tag.db', check_same_thread=False)
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS tags
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              input_text TEXT,
              tags TEXT,
              created_at TEXT)''')

conn.commit()


@tag.route("/tag", methods=["GET", "POST"])
def home():
    search_text = request.args.get("search_text", "")
    if search_text:
        c.execute("SELECT * FROM tags WHERE tags LIKE ?", ('%'+search_text+'%',))
        tags_list = c.fetchall()
        return render_template("diary/grammar.html", search_text=search_text, tags_list=tags_list)

    return render_template("diary/grammar.html")

@tag.route("/search_tags")
def search_tags():
    query = request.args.get("query")
    c.execute("SELECT * FROM tags WHERE tags LIKE ?", ("%" + query + "%",))
    results = c.fetchall()
    return render_template("diary/tagindex.html", results=results)


@tag.route("/generate_tags", methods=["POST"])
def generate_tags():
    input_text = request.form["input_text"]
    inputs = tokenizer([input_text], max_length=512, truncation=True, return_tensors="pt")
    output = model.generate(**inputs, num_beams=8, do_sample=True, min_length=10,
                            max_length=64)
    decoded_output = tokenizer.batch_decode(output, skip_special_tokens=True)[0]
    tags = list(set(decoded_output.strip().split(", ")))

    return render_template("diary/tagindex.html", tags=tags)


if __name__ == '__main__':
    tag.run(debug=True)

conn.close()