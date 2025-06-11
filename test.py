import flask
import cv2
import numpy as np
import base64
import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS  # For Cross-Origin Requests

# Load the trained model
with open('./model.p', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)
CORS(app)  # Enable CORS to allow communication with the frontend

# Store detected sentence
sentence = []

# Image preprocessing function
def preprocess_frame(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    frame = cv2.resize(frame, (64, 64))  # Resize to match model input
    frame = frame / 255.0  # Normalize
    frame = frame.reshape(1, 64, 64, 1)  # Reshape for model
    return frame

@app.route('/detect', methods=['POST'])
def detect_sign():
    try:
        data = request.json.get('data')
        if not data:
            return jsonify({'error': 'No image data received'}), 400

        # Decode Base64 image
        image_data = base64.b64decode(data.split(',')[1])
        np_arr = np.frombuffer(image_data, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        if frame is None:
            return jsonify({'error': 'Invalid image format'}), 400

        # Process image
        processed_frame = preprocess_frame(frame)

        # Predict using model
        prediction = model.predict(processed_frame)
        predicted_character = chr(int(np.argmax(prediction)) + 65)  # Convert index to letter

        # Display detected character
        print(f"Detected Character: {predicted_character}")

        return jsonify({'result': predicted_character})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
