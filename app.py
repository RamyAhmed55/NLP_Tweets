import joblib

load_model = joblib.load("sentiment_model.pkl")

from flask import Flask, request, jsonify

app = Flask(__name__)


# define prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    # receive data
    data = request.get_json(force=True)  
    text = data.get("text", "")           
    
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    
    prediction = load_model.predict([text])[0]
    
    # return result
    return jsonify({"prediction": prediction})



# Run the app
if __name__ == "__main__":
    app.run(debug=True)
