# 🧏‍♂️ Sign Language Detection & Translation System 🤖

## 🎓 Graduation Project

A smart, interactive web-based system that detects and translates sign language in real-time using deep learning and computer vision. Designed to enhance communication between hearing-impaired individuals and the hearing community by recognizing hand gestures and converting them into readable text or audible speech.

----

## 🚀 Key Features

- **🖐️ Real-Time Sign Language Detection**  
  Utilizes a Random Forest classifier and webcam feed to detect alphabetic hand signs and dynamically construct words and sentences. Features include:
  - Adding spaces
  - Deleting characters
  - Selecting predefined words or actions

- **🖼️ Image-Based Sign Classification**  
  A custom CNN model trained on Indian Sign Language (ISL) to classify static images of hand gestures with high accuracy.

- **💬 Text-to-Sign Language Chatbot**  
  A user-friendly chatbot that converts typed sentences into a sequence of sign images to assist deaf users.

---

## 🛠️ Technologies Used

- **Frontend:** Angular, HTML, CSS, JavaScript  
- **Backend:** Flask / Django (if applicable)  
- **Machine Learning & Vision:**  
  - Python  
  - OpenCV  
  - NumPy  
  - MediaPipe  
  - TensorFlow / Keras  
  - Scikit-learn (Random Forest)  
  - Custom CNN Model  
- **Design:** Figma (for UI/UX prototypes)

---

## 🌐 How It Works

1. **Real-Time Mode**  
   Uses webcam input to detect hand gestures. The model processes each frame, classifies the sign, and displays the corresponding character on-screen, building full sentences.

2. **Image Upload Mode**  
   Upload or capture an image. The image is processed and passed to a CNN model for classification based on trained ISL data.

3. **Chatbot Mode**  
   Enter any text, and the system will return visual sign language equivalents to communicate with deaf users.

---

## 📦 Project Structure

