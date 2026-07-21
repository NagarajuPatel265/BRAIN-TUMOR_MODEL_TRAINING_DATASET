import numpy as np
import tensorflow as tf
import cv2
import os

# ======================================
# Model Configuration
# ======================================

MODEL_PATH = "model/BrainTumor_EfficientNetB0.keras"

model = None

# ======================================
# Class Names
# ======================================

class_names = [
    "Glioma",
    "Meningioma",
    "No Tumor",
    "Pituitary"
]

IMG_SIZE = 224

# ======================================
# Allowed Image Extensions
# ======================================

ALLOWED_EXTENSIONS = (".jpg", ".jpeg", ".png")

# ======================================
# Load Model
# ======================================

def load_model():

    global model

    if model is None:

        print("=" * 60, flush=True)
        print("Loading TensorFlow model...", flush=True)

        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

        model = tf.keras.models.load_model(MODEL_PATH)

        print("Model loaded successfully.", flush=True)
        print("=" * 60, flush=True)

# ======================================
# Image Preprocessing
# ======================================

def preprocess_image(image_path):

    print("A. Checking image path...", flush=True)

    if not os.path.exists(image_path):
        raise ValueError("Image file not found.")

    print("B. Image found.", flush=True)

    if not image_path.lower().endswith(ALLOWED_EXTENSIONS):
        raise ValueError("Only JPG, JPEG and PNG images are allowed.")

    print("C. Reading image...", flush=True)

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Unable to read the uploaded image.")

    print("D. Image loaded.", flush=True)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    print("E. Image converted to RGB.", flush=True)

    image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))

    print("F. Image resized.", flush=True)

    image = image.astype(np.float32)

    image = image / 255.0

    image = np.expand_dims(image, axis=0)

    print("G. Preprocessing completed.", flush=True)

    return image

# ======================================
# Prediction Function
# ======================================

def predict_tumor(image_path):

    print("=" * 60, flush=True)
    print("Prediction Started", flush=True)

    load_model()

    print("1. Model Ready", flush=True)

    image = preprocess_image(image_path)

    print("2. Calling model.predict()", flush=True)

    prediction = model.predict(image, verbose=0)[0]

    print("3. model.predict() completed", flush=True)

    predicted_index = np.argmax(prediction)

    predicted_class = class_names[predicted_index]

    confidence = float(prediction[predicted_index] * 100)

    probabilities = {}

    for i, cls in enumerate(class_names):
        probabilities[cls] = round(float(prediction[i] * 100), 2)

    print("Prediction:", predicted_class, flush=True)
    print("Confidence:", confidence, flush=True)
    print("Prediction Finished", flush=True)
    print("=" * 60, flush=True)

    return predicted_class, confidence, probabilities

# ======================================
# Local Testing
# ======================================

if __name__ == "__main__":

    test_image = "sample.jpg"

    if os.path.exists(test_image):

        pred, conf, probs = predict_tumor(test_image)

        print("\nPrediction :", pred)
        print("Confidence :", round(conf, 2), "%")

        print("\nProbabilities")
        print("---------------------------")

        for k, v in probs.items():
            print(f"{k:15} : {v}%")

    else:
        print("sample.jpg not found.")