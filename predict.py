import numpy as np
import tensorflow as tf
import cv2
import os

# ======================================
# Load Model
# ======================================

MODEL_PATH = "model/BrainTumor_EfficientNetB0.keras"

model = tf.keras.models.load_model(MODEL_PATH)

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
# Image Preprocessing
# ======================================

def preprocess_image(image_path):

    # Check File Exists

    if not os.path.exists(image_path):
        raise ValueError("Image file not found.")

    # Check Extension

    if not image_path.lower().endswith(ALLOWED_EXTENSIONS):
        raise ValueError(
            "Only JPG, JPEG and PNG images are allowed."
        )

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(
            "Unable to read the uploaded image."
        )

    image = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2RGB
    )

    image = cv2.resize(
        image,
        (IMG_SIZE, IMG_SIZE)
    )

    image = image.astype(np.float32)

    image = image / 255.0

    image = np.expand_dims(
        image,
        axis=0
    )

    return image

# ======================================
# Prediction Function
# ======================================

def predict_tumor(image_path):

    image = preprocess_image(image_path)

    prediction = model.predict(
        image,
        verbose=0
    )[0]

    predicted_index = np.argmax(prediction)

    predicted_class = class_names[predicted_index]

    confidence = float(
        prediction[predicted_index] * 100
    )

    probabilities = {}

    for i, cls in enumerate(class_names):

        probabilities[cls] = round(
            float(prediction[i] * 100),
            2
        )

    return (
        predicted_class,
        confidence,
        probabilities
    )

# ======================================
# Test
# ======================================

if __name__ == "__main__":

    image_path = "sample.jpg"

    if os.path.exists(image_path):

        pred, conf, probs = predict_tumor(image_path)

        print()

        print("Prediction :", pred)

        print("Confidence :", round(conf,2), "%")

        print()

        print("Probabilities")

        print("------------------------")

        for k,v in probs.items():

            print(f"{k:15} : {v}%")

    else:

        print("sample.jpg not found.")