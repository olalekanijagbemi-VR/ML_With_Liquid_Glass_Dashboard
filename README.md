# 🍄 Mushroom ML Classifier

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.1%2B-green)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.9%2B-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🚀 Overview

A **stunning Liquid Glass ML web application** that classifies mushrooms as **edible or poisonous** using Support Vector Machines, Logistic Regression, and Random Forest models – with real-time customizable glass effects.

**Live Demo:** [https://ml-with-liquid-glass-dashboard.onrender.com](https://ml-with-liquid-glass-dashboard.onrender.com)

---

## ✨ Key Features

### 🧠 ML Classification
- **3 Classifiers**: SVM, Logistic Regression, Random Forest
- **Hyperparameter tuning** (C, max_iter, max_depth)
- **Real-time training** with metrics (Accuracy, Precision, Recall)
- **Confusion Matrix & ROC Curve** visualizations
- **Raw data preview**

### 🎨 Liquid Glass UI
- **Real-time Shader Panel** (Blur, Frost, Tint, Bevel, Specular, Depth, Radius, Contrast, Brightness)
- **Text Color Changer** (White, Black, Blue, Red, Yellow, Green)
- **4 Background images/GIFs** with switcher
- **Glassmorphism cards** with 3D depth + hover glow
- **Fully responsive**

---

## 📂 Project Structure
Mushroom_ML_Classifier/
├── app.py # Main Flask application
├── Dockerfile # Docker configuration
├── requirements.txt # Python dependencies
├── mushrooms.csv # Dataset (8,124 rows)
├── static/
│ ├── images/ # Background images
│ └── ml-dashboard.html # Liquid Glass UI
└── README.md


---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.11+** | Backend |
| **Flask** | Web framework |
| **scikit-learn** | ML models |
| **pandas** | Data processing |
| **matplotlib** | Charts |
| **HTML/CSS/JS** | Liquid Glass UI |

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/olalekanijagbemi-VR/ML_With_Liquid_Glass_Dashboard.git
cd ML_With_Liquid_Glass_Dashboard
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
# Open http://127.0.0.1:5001

📸 Screenshots
Main Dashboard
https://screenshots/dashboard.png

Training Results
https://screenshots/results.png

Shader Panel
https://screenshots/shader_panel.png

👨‍💻 Author
Olalekan Ijagbemi

GitHub  https://github.com/olalekanijagbemi-VR

LinkedIn https://www.linkedin.com/in/olalekan-ijagbemi-95a1b2269/

📄 License
MIT License