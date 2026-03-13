import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("data/knowledge_base.csv")

questions = data["question"]
answers = data["answer"]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

model = LogisticRegression()
model.fit(X, answers)

pickle.dump(model, open("model/chatbot_model.pkl","wb"))
pickle.dump(vectorizer, open("model/vectorizer.pkl","wb"))

print("Model trained successfully")
