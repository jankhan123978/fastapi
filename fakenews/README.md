# 📰 Fake News Classifier API

A FastAPI-based web application that classifies news as **real** or **fake** using a trained machine learning model.

---

## 🚀 Features

- ✅ Predicts whether input news text is real or fake
- 🧠 Uses a trained machine learning model (with vectorizer)
- 🌐 Built with [FastAPI](https://fastapi.tiangolo.com/)
- 🖥️ Simple web UI with HTML & CSS
- 📦 Easily deployable via platforms like Render, Railway, or Replit

---

## 📁 Project Structure
fakenews/
├── app.py # Main FastAPI app
├── model/
│ ├── model.pkl # Trained ML model
│ └── vectorizer.pkl # Fitted TF-IDF vectorizer
├── templates/
│ └── index.html # Web interface
├── static/
│ └── style.css # CSS styling
├── requirements.txt # Python dependencies
└── .gitignore

