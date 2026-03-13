# Collaborative NLP-Based College Information Chatbot

## Overview

The **Collaborative NLP-Based College Information Chatbot** is an AI-powered chatbot designed to assist students by providing instant answers to common college-related queries such as admissions, courses, fees, exams, facilities, and placements.

The chatbot uses **Natural Language Processing (NLP)** techniques to understand student questions and provide relevant responses from a knowledge base.

This project demonstrates the use of **machine learning and conversational AI** to improve student support services in educational institutions.

---

## Features

* NLP-based question understanding
* Interactive chatbot interface
* Instant answers to student queries
* CSV-based knowledge base
* Admin panel to add new questions and answers
* Machine learning model for intent matching
* Lightweight and easy to deploy

---

## Technologies Used

* Python
* Flask
* Scikit-learn
* Natural Language Processing (NLP)
* HTML
* CSS
* JavaScript
* Pandas

---

## Project Structure

```
college-nlp-chatbot
│
├── app.py
├── train.py
├── requirements.txt
│
├── data
│   └── knowledge_base.csv
│
├── model
│   ├── chatbot_model.pkl
│   └── vectorizer.pkl
│
├── templates
│   ├── index.html
│   └── admin.html
│
└── static
    ├── style.css
    └── script.js
```

---

## Installation and Setup

### 1. Clone the Repository

```
git clone https://github.com/heetruparel/college-nlp-chatbot.git
```

### 2. Navigate to the Project Folder

```
cd college-nlp-chatbot
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Train the Chatbot Model

```
python train.py
```

### 5. Run the Application

```
python app.py
```

### 6. Open in Browser

```
http://127.0.0.1:5000
```

---

## Admin Panel

The admin panel allows adding new questions and answers to the chatbot database.

Access it at:

```
http://127.0.0.1:5000/admin
```

---

## Example Queries

Students can ask questions such as:

* What courses are offered?
* What is the BCA fee?
* When are semester exams?
* Do you provide hostel facilities?
* What are the college timings?
* Where is the library?

---

## Future Improvements

Possible enhancements for this project include:

* Integration with voice assistants
* Deployment on cloud platforms
* Improved NLP using transformer-based models
* Integration with student portals
* WhatsApp chatbot integration

---

## Author

Heet Ruparel

---

## License

This project is developed for educational purposes.
