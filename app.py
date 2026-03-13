from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("model/chatbot_model.pkl","rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    X = vectorizer.transform([user_message])
    reply = model.predict(X)[0]
    return jsonify({"reply": reply})

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/add", methods=["POST"])
def add_data():
    question = request.form["question"]
    answer = request.form["answer"]

    df = pd.read_csv("data/knowledge_base.csv")
    df.loc[len(df)] = [question, answer]
    df.to_csv("data/knowledge_base.csv", index=False)

    return "Added successfully. Please retrain model."

if __name__ == "__main__":
    app.run(debug=True)
