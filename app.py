from flask import Flask, jsonify, request
from utilities import predict_pipeline
import streamlit
from  utilities  import show_predict_page
app = Flask(__name__)

@app.post('/predict')
def predict():
    data = request.json
    try:
        sample = data['text']
    except KeyError:
        return jsonify({'error':'No text was sent'})
    sample = [sample]
    predictions = predict_pipeline(sample)
    try:
        result = jsonify(predictions[0])
    except TypeError as e: 
        return jsonify({'error':str(e)})
    return result
show_predict_page()

