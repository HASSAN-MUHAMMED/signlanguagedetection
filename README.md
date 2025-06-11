# Sign Language Detection & Translation System 🧏‍♂️🤖

## 🎓 Graduation Project

This web-based system is designed to detect and translate sign language in real-time, helping bridge the communication gap between hearing-impaired individuals and others. It combines computer vision and deep learning to recognize hand signs and translate them into text or speech.

---

## 🚀 Features

- **Real-Time Detection Model**  
  Uses a Random Forest classifier to recognize hand signs via webcam and build sentences letter by letter. Includes support for:
  - Adding spaces
  - Deleting characters
  - Selecting predefined words

- **Image-Based Detection Model**  
  Based on transfer learning using the VGG16 model to classify static images according to Indian Sign Language.

- **Text-to-Sign Chatbot**  
  A simple chatbot interface that converts typed text into sign language visuals for deaf users.

---

## 🛠️ Technologies Used

- Python
- OpenCV
- TensorFlow / Keras
- Scikit-learn (Random Forest)
- VGG16 (Transfer Learning)
- Flask / Django (if applicable)
- HTML, CSS, JavaScript

---

## 🌐 How It Works

1. **Real-Time Mode**  
   Open your webcam and start performing sign gestures. The system will detect letters, build words/sentences, and display the results instantly.

2. **Image Upload Mode**  
   Upload or capture an image of a hand sign. The system will classify it using the VGG16 model trained on Indian Sign Language.

3. **Chatbot Mode**  
   Type any sentence, and the bot will return corresponding sign gestures to display for deaf users.

---

### 📁 Project Structure

