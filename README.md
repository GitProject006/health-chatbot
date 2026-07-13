# Disease Awareness Health Chatbot

A web-based health chatbot developed using **Python**, **Flask**, and **Machine Learning** to predict possible diseases from user-entered symptoms and provide disease awareness information. This project was created as part of a Python learning project to demonstrate the integration of machine learning with web development.

> **Disclaimer:** This application is intended for educational and awareness purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment.

##  Live Demo

🌐 https://disease-awareness-chatbot.onrender.com/

##  Features

- Predicts possible diseases based on symptoms entered by the user.
- Displays the most likely disease predictions.
- Provides disease awareness information, including:
  - Symptoms
  - Causes
  - Prevention
  - Treatment
- Simple and interactive chatbot interface.
- Deployed as a web application using Render.

---

##  Tech Stack

### Backend
- Python
- Flask

### Machine Learning
- scikit-learn
- NumPy

### Deployment
- Gunicorn
- Render

### Frontend
- HTML
- CSS
- JavaScript

---

##  Machine Learning Model

The chatbot uses Natural Language Processing (NLP) techniques to process symptom descriptions.

- **CountVectorizer** for converting symptom text into numerical features.
- **Multinomial Naive Bayes** classifier for disease prediction.
- A custom JSON knowledge base containing disease information.

---

##  Project Structure

```text
health-chatbot/
│
├── health_chatbot/
│   ├── app.py
│   ├── chatbot.py
│   ├── symptom_model.py
│   ├── diseases.json
│   ├── requirements.txt
│   └── templates/
│       └── index.html
│
└── README.md
```

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/GitProject006/health-chatbot.git
```

Move into the project directory:

```bash
cd health-chatbot/health_chatbot
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

##  Dependencies

- Flask
- scikit-learn
- NumPy
- Gunicorn

---

## 💡 Future Improvements

- Improve prediction accuracy with larger datasets.
- Support multiple languages.
- Add user authentication and history.
- Integrate with healthcare APIs.
- Enhance the chatbot interface and user experience.

---

##  Author

**Riya**

B.Tech Computer Science and Engineering  
SRM University-AP
