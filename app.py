from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from predict import predict_tumor

app = Flask(__name__)

# ===========================================
# Upload Folder
# ===========================================

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ===========================================
# Allowed Extensions
# ===========================================

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}

def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )

# ===========================================
# Home Page
# ===========================================

@app.route("/")
def home():
    return render_template("index.html")

# ========================.
# ===================
# Prediction Route
# ===========================================

@app.route("/predict", methods=["POST"])
def predict():

    # Check whether file exists

    if "image" not in request.files:

        return render_template(
            "result.html",
            prediction="No Image Uploaded",
            confidence="0%",
            probabilities={},
            image=None
        )

    file = request.files["image"]

    # Check filename

    if file.filename == "":

        return render_template(
            "result.html",
            prediction="No Image Selected",
            confidence="0%",
            probabilities={},
            image=None
        )

    # Check extension

    if not allowed_file(file.filename):

        return render_template(
            "result.html",
            prediction="Invalid File",
            confidence="Only JPG, JPEG and PNG images are allowed.",
            probabilities={},
            image=None
        )

    # Save Image

    filename = secure_filename(file.filename)

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(filepath)

    try:

        prediction, confidence, probabilities = predict_tumor(filepath)

        return render_template(
            "result.html",
            prediction=prediction,
            confidence=f"{confidence:.2f}%",
            probabilities=probabilities,
            image=filename
        )

    except Exception as e:

        return render_template(
            "result.html",
            prediction="Prediction Failed",
            confidence=str(e),
            probabilities={},
            image=None
        )

# ===========================================
# Run Flask
# ===========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )