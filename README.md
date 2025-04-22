# 👁️‍🗨️ Privacy Facial Detection System

This is a Python-based real-time facial detection system using OpenCV. It detects multiple faces and eyes in a webcam feed and displays an alert when more than one face is detected — useful for privacy-focused applications like secure login or private screen access.

---

## 🧠 Features

- 🔍 Real-time face and eye detection using Haar Cascade classifiers
- 🚨 Privacy alert when more than one face is detected
- 📸 Webcam integration (can switch between multiple cameras)
- 📦 Easy to extend with more detection models (e.g., mouth, smile, etc.)

---

## 📁 Project Structure
privacy-facial-detection/ ├── data/ │ └── raw/ │ ├── haarcascade_frontalface_default.xml │ └── rawDataEye.xml ├── facial_reg.py ├── README.md └── .venv/

## ⚙️ Requirements

- Python 3.7+
- OpenCV 
- Webcam

### Install dependencies:
```bash
pip install opencv-python
```

### 🚀 How to Run
Make sure your .xml cascade files are in the correct data/raw path.

Then run:
python facial_reg.py

Press q to quit the webcam stream.

### 📷 Camera Settings
If your default camera doesn't work, change:

video_cam = cv2.VideoCapture(0)  # Try 1 or 2 if 0 doesn't work

### 🔒 Privacy Alert
When the system detects two or more faces, a red warning appears on the screen and is also printed to the terminal:

### 🧩 To-Do / Enhancements
 Use cv2.dnn or MediaPipe for more accurate face detection

 Add facial recognition (identify users)

 Mask detection

 Record logs of intrusions (time, frame)

 Email or notification on privacy breach

 
---

Let me know if you want me to customize it further — like adding GIFs, usage images, or linking to your GitHub profile.

