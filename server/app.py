# server/app.py

from flask import Flask, jsonify, session, make_response
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "supersecretkey"  
CORS(app)  


ARTICLES = [
    {"id": 1, "title": "Article 1", "content": "This is the content of Article 1."},
    {"id": 2, "title": "Article 2", "content": "This is the content of Article 2."},
    {"id": 3, "title": "Article 3", "content": "This is the content of Article 3."},
    {"id": 4, "title": "Article 4", "content": "This is the content of Article 4."},
    {"id": 5, "title": "Article 5", "content": "This is the content of Article 5."},
]

@app.route("/articles/<int:id>", methods=["GET"])
def show_article(id):
    
    session['page_views'] = session.get('page_views') or 0

    
    session['page_views'] += 1

    
    if session['page_views'] > 3:
        return make_response(
            jsonify({"message": "Maximum pageview limit reached"}),
            401
        )

    
    article = next((a for a in ARTICLES if a["id"] == id), None)

    if not article:
        return make_response(jsonify({"message": "Article not found"}), 404)

    return jsonify(article)

@app.route("/clear", methods=["GET"])
def clear_session():
    session.clear()
    return jsonify({"message": "Session cleared"})

if __name__ == "__main__":
    app.run(port=5555, debug=True)
