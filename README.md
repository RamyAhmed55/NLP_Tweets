# Sentiment Analysis Project

This project builds a sentiment analysis model to classify text as **positive** or **negative**.  
It includes data preprocessing, model training, evaluation, saving the best pipeline, and deploying it as a simple Flask API.

---

## Project Structure
project-folder/
│
├── notebook.ipynb          # Jupyter Notebook with preprocessing, training, evaluation
├── app.py                  # Flask API to serve predictions
├── sentiment_model.pkl     # Saved trained pipeline (best model)
├── requirements.txt        # Dependencies to run the project
└── README.md               # Project documentation

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repo-link>
   cd project-folder


2) Install dependencies:

pip install -r requirements.txt

## Run the API

* Start the Flask server:

python app.py

* The server will run on:
http://127.0.0.1:5000/

## Test the API

* Use curl or Postman to send a request:

curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d "{\"text\": \"I love this project!\"}"


* Response:
{"prediction": "positive"}



