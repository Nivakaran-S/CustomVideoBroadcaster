# End-to-End Custom Video Broadcaster with Background Replacement for Google Meet

Transform your video call experience by customizing your video feed with blurred or virtual backgrounds — directly in Google Meet or Zoom. This project bridges the gap between frame-based video processing and real-time video streaming, using OpenCV, YOLOv8, FastAPI, and OBS virtual camera.

## 🚀 Project Overview
Google Meet and Zoom expect a continuous video stream from your camera, but computer vision libraries like OpenCV only provide individual frames. This creates a challenge when applying real-time computer vision processing — such as background blurring or replacement.

This project solves that by:
- Mimicking a physical webcam using a virtual one.
- Feeding processed frames (blurred/custom background) into this virtual webcam.
- Allowing you to use the modified video stream in Google Meet, Zoom, or any other video conferencing software.

## 🧠 Problem Statement
🧩 The Issue: When you apply image processing using OpenCV, you get individual frames — not a video stream. But platforms like Google Meet require a continuous stream (like from a physical webcam).

## 💡 Solution
✅ The Fix: We create a virtual webcam using OBS (Open Broadcaster Software) and pyvirtualcam, allowing us to send processed video frames as a continuous stream.

How It Works:
[Your Webcam] → [OpenCV Processing] → [pyvirtualcam] → [OBS Virtual Camera] → [Google Meet / Zoom]

## 🛠️ Tech Stack
- Backend: Python, FastAPI
- Frontend: HTML, JavaScript
- Computer Vision: OpenCV, YOLOv8 (medium model), Image Segmentation
- Streaming: pyvirtualcam
- Virtual Webcam: OBS Studio + Virtual Camera Driver

## ✨ Features
- Human Segmentation using YOLOv8
- Custom Background Support
- Background Blur
- Real-Time Streaming
- Web-Based Interface
- Plug and Play for Google Meet or Zoom

## 🧪 Prerequisites
1. OBS Studio (https://obsproject.com/)
2. Python 3.8 or above
3. Git

## 📦 Installation
```
git clone https://github.com/yourusername/custom-video-broadcaster.git
cd custom-video-broadcaster
python -m venv venv
source venv/bin/activate  (On Windows: venv\Scripts\activate)
pip install -r requirements.txt
```

## ▶️ Running the App
1. Start OBS Virtual Camera
2. Run the FastAPI backend: uvicorn app.main:app --reload
3. Open: http://127.0.0.1:8000
4. Choose mode: Background Blur / Add Custom Background
5. Select "OBS Virtual Camera" in Google Meet or Zoom


## 🧠 How Does Human Segmentation Work?
- Uses YOLOv8m for detection
- Applies mask-based segmentation
- Blurs or replaces non-human regions

## 📁 Project Structure
```
app/
├── main.py            
├── video_utils.py     
static/
├── index.html         
requirements.txt
README.md
```

## ❗ Limitations
- OBS can't stream to multiple apps simultaneously
- Dependent on system hardware
- Best performance with good lighting

## ✅ To-Do / Future Improvements
- Webcam selection UI
- Use MediaPipe for segmentation
- Video background support
- Docker support
- OBS session recording

## 📚 References
- https://obsproject.com/wiki/
- https://docs.ultralytics.com/
- https://github.com/letmaik/pyvirtualcam
- https://fastapi.tiangolo.com/

## 🏁 Final Words
This project demonstrates how you can bridge the gap between computer vision and real-time applications, creatively mimicking hardware functionality through software. It's a practical, real-world application of machine learning, video streaming, and system-level programming — ideal for live video enhancements, privacy, and personalization.
