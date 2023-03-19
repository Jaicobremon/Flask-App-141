from flask import Flask, jsonify, request
import csv

all_articles = []

with open("articles.csv",encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []
did_not_read_articles = []

app = Flask(__name__)
@app.route("/get-article")

def get_article():
    if len(all_articles) == 0:
        return jsonify({
            "error":"No articles left"
        }),404
    article = all_articles[0]
    all_articles = all_articles[1:]
    return jsonify({
        "data":article,
        "status":"Success"
    })

@app.route("/liked-article",methods = ["POST"])

def liked_article():
    global all_articles
    if len(all_articles) == 0:
        return jsonify({
            "error":"No articles left"
        }),404
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)

    return jsonify({
        "status":"Success"
    }),201

@app.route("/unliked-article",methods = ["POST"])

def unliked_article():
    global all_articles
    if len(all_articles) == 0:
        return jsonify({
            "error":"No articles left"
        }),404
    article = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(article)

    return jsonify({
        "status":"Success"
    }),201

@app.route("/did-not-read-article",methods = ["POST"])

def did_not_read_article():
    global all_articles
    if len(all_articles) == 0:
        return jsonify({
            "error":"No articles left"
        }),404
    article = all_articles[0]
    all_articles = all_articles[1:]
    did_not_read_articles.append(article)

    return jsonify({
        "status":"Success"
    }),201

if __name__ == "__main__":
    app.run()