# 🖼️ Smart Image Annotation System

> An AI-powered object detection and image annotation application built using **Python**, **YOLOv8s**, and **Streamlit**. The system automatically detects multiple objects in uploaded images, annotates them with bounding boxes, displays detection statistics, and generates downloadable reports.

---
## 📖 Brief Project Description

The **Smart Image Annotation System** is an AI-powered computer vision application developed using **Python**, **YOLOv8s**, and **Streamlit**. It enables users to upload an image, automatically detect multiple objects, and annotate them with bounding boxes and confidence scores. The application also provides image information, object counts, detection statistics, and detailed detection reports that can be downloaded in **CSV** and **PDF** formats. Designed with a simple and interactive interface, this project demonstrates the practical application of Artificial Intelligence, Deep Learning, and Computer Vision in automated image annotation.

# 🔗 GitHub Repository

**Repository Link:** *https://github.com/Harmankaur07/smart_image_annotation/upload*

# 📌 Project Overview

The **Smart Image Annotation System** is a computer vision application that utilizes the **YOLOv8s (You Only Look Once)** deep learning model to detect and annotate objects in images.

Users can upload an image, perform object detection, view annotated results, analyze detection statistics, and download reports in multiple formats. The application provides a simple, interactive, and user-friendly interface built with Streamlit.

This project was developed as a **Summer Training Project (2026)** to enhance practical knowledge in **Artificial Intelligence, Computer Vision, and Deep Learning**.

---

# ✨ Features

- ✅ Upload JPG, JPEG, and PNG images
- ✅ Object Detection using YOLOv8s
- ✅ Adjustable Confidence Threshold
- ✅ Automatic Image Annotation
- ✅ Bounding Boxes with Confidence Scores
- ✅ Detection Summary
- ✅ Detection Statistics
- ✅ Object Counter
- ✅ Object Details Table
- ✅ Image Information
  - Width
  - Height
  - Image Format
  - Color Mode
  - File Size
- ✅ Original & Annotated Image Display
- ✅ Automatically Save Annotated Image
- ✅ Automatically Save CSV Detection Report
- ✅ Automatically Save PDF Detection Report
- ✅ Download Annotated Image
- ✅ Download CSV Detection Report
- ✅ Download PDF Detection Report
- ✅ Processing Time Measurement
- ✅ Interactive Streamlit User Interface

---

# 🏗️ System Workflow

```text
User Uploads Image
        │
        ▼
Image Preprocessing
        │
        ▼
YOLOv8s Object Detection
        │
        ▼
Bounding Box Annotation
        │
        ▼
Detection Summary & Statistics
        │
        ▼
Object Counter
        │
        ▼
Report Generation
        │
        ▼
Download Annotated Image / CSV / PDF
```

---

# 📂 Project Structure

```text
Smart_Image_Annotation_System/
│
├── app.py
├── detector.py
├── annotation.py
├── image_info.py
├── report.py
├── object_counter.py
├── requirements.txt
├── README.md
│
├── models/
│   └── yolov8s.pt
│
├── images/
│
├── outputs/
```

---

# ⚙️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Application Framework |
| YOLOv8s | Object Detection Model |
| Ultralytics | YOLO Framework |
| OpenCV | Image Processing |
| Pillow (PIL) | Image Handling |
| Pandas | Data Processing |
| NumPy | Numerical Computation |
| Matplotlib | Data Visualization |
| ReportLab | PDF Report Generation |

---

# 📦 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Harmankaur07Annotation-System.git
```


---

## 2️⃣ Open the Project Folder

```bash
cd Smart-Image-Annotation-System
```

---

## 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run the Application

Use the following command:

```bash
python -m streamlit run app.py
```


---

# 🖥️ How to Use

### Step 1

Run the Streamlit application.

### Step 2

Upload an image in one of the following formats:

- JPG
- JPEG
- PNG

### Step 3

Adjust the confidence threshold using the sidebar slider.

### Step 4

Click **Detect Objects**.

### Step 5

The application displays:

- Image Information
- Detection Summary
- Detection Statistics
- Object Counter
- Object Details Table
- Original Image
- Annotated Image
- Processing Time

### Step 6

Download:

- Annotated Image
- CSV Detection Report
- PDF Detection Report

---

# 📊 Output Information

# 📊 Output Information

The application generates the following outputs:

- Total Objects Detected
- Unique Object Classes
- Object Counts
- Confidence Scores
- Detection Statistics
- Image Information
- Processing Time
- Annotated Image
- CSV Detection Report
- PDF Detection Report

All generated output files are automatically saved in the **outputs/** folder for future reference and can also be downloaded directly through the Streamlit application.

---

# 🎯 Applications

- Smart Image Annotation
- Object Detection
- Computer Vision
- Artificial Intelligence
- Machine Learning
- Dataset Annotation
- Educational Projects
- Research & Development

---

# 🚀 Future Enhancements

- Multiple Image Upload
- Batch Image Processing
- Detection History
- Excel Report Export
- Object Search
- Real-Time Webcam Detection
- Cloud Deployment
- Interactive Dashboard

---

# 💻 Developer

**Harman Kaur**

**B.Tech – Computer Science & Engineering**

**Summer Training Project – 2026**

---

# 🙏 Acknowledgements

This project was developed using the following open-source technologies:

- Ultralytics YOLOv8
- Streamlit
- OpenCV
- ReportLab
- Python Community

Special thanks to the developers and contributors of these technologies for making this project possible.

---

# 📜 License

This project is developed for **educational and learning purposes** as part of a Summer Training Program.

---

# ⭐ Support

If you found this project useful or interesting, consider giving it a ⭐ on GitHub.

---

# 📧 Contact

**Developer:** Harman Kaur

**Project:** Smart Image Annotation System

**Year:** 2026
