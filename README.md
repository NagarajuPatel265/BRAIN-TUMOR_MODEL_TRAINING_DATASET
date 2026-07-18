# 🧠 Brain Tumor Detection Using Deep Learning

A web-based Brain Tumor Detection system built using **Flask**, **TensorFlow**, and **EfficientNetB0**. The application allows users to upload brain MRI images and predicts whether a tumor is present along with the tumor class.

---

## 📌 Features

- 🧠 Brain MRI image classification
- 🚀 Deep Learning model using EfficientNetB0
- 🌐 User-friendly Flask web interface
- 📤 Image upload functionality
- 📊 Displays prediction results with confidence
- 📱 Responsive web design

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3

### Backend
- Python
- Flask

### Deep Learning
- TensorFlow
- Keras
- EfficientNetB0

### Libraries
- NumPy
- OpenCV
- Pillow
- Pickle

---

## 📂 Project Structure

```
Braintumor/
│
├── app.py
├── predict.py
├── requirements.txt
├── brain_tumor_labels.pkl
├── best_model.keras
├── model/
│   └── BrainTumor_EfficientNetB0.keras
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── uploads/
│
└── README.md
```

---

## 📊 Dataset

The model is trained on Brain MRI images containing multiple tumor classes.

Example classes include:

- Glioma
- Meningioma
- Pituitary Tumor
- No Tumor

> **Note:** The dataset is not included in this repository because of GitHub's file size limitations.

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/NagarajuPatel265/BRAIN-TUMOR_MODEL_TRAINING_DATASET.git
```

### Move into the project folder

```bash
cd BRAIN-TUMOR_MODEL_TRAINING_DATASET
```

### Create a virtual environment (Optional)

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🧪 How to Use

1. Open the web application.
2. Upload a brain MRI image.
3. Click the **Predict** button.
4. View the predicted tumor class and confidence score.

---

## 📸 Screenshots

### Home Page

<img width="1907" height="893" alt="Screenshot 2026-07-18 165044" src="https://github.com/user-attachments/assets/9df92ea4-6c7e-45de-b97e-0aa8387ede41" />


### Prediction Result
<img width="1907" height="887" alt="Screenshot 2026-07-18 165135" src="https://github.com/user-attachments/assets/7a3efaf5-51c8-45b5-af94-6ae40961b26c" />



---

## 📈 Model Information

| Model | EfficientNetB0 |
|--------|----------------|
| Framework | TensorFlow / Keras |
| Input Size | 224 × 224 |
| Image Type | Brain MRI |
| Task | Multi-Class Classification |

---

## 🚀 Future Improvements

- Support more tumor categories
- Upload multiple images
- Deploy using Render or Railway
- User authentication
- Patient history storage
- Grad-CAM visualization for model explainability

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push to your branch.
5. Create a Pull Request.

---

## 📄 License

This project is intended for educational and research purposes.

---

## 👨‍💻 Author

**Nagaraju Puppala**

- GitHub: https://github.com/NagarajuPatel265
- LinkedIn: www.linkedin.com/in/nagaraju-puppala2605

---

⭐ If you found this project helpful, consider giving it a star!
