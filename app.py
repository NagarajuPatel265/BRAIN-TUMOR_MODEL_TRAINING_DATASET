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
    print("Home page loaded", flush=True)
    return render_template("index.html")

# ===========================================
# Prediction Route
# ===========================================

@app.route("/predict", methods=["POST"])
def predict():

    print("=" * 60, flush=True)
    print("STEP 1: /predict request received", flush=True)

    try:

        # Check whether file exists
        if "image" not in request.files:
            print("STEP 2: No image found in request", flush=True)

            return render_template(
                "result.html",
                prediction="No Image Uploaded",
                confidence="0%",
                probabilities={},
                image=None
            )

        file = request.files["image"]

        print("STEP 3: Image received", flush=True)

        # Check filename
        if file.filename == "":
            print("STEP 4: Empty filename", flush=True)

            return render_template(
                "result.html",
                prediction="No Image Selected",
                confidence="0%",
                probabilities={},
                image=None
            )

        # Check extension
        if not allowed_file(file.filename):
            print("STEP 5: Invalid file extension", flush=True)

            return render_template(
                "result.html",
                prediction="Invalid File",
                confidence="Only JPG, JPEG and PNG images are allowed.",
                probabilities={},
                image=None
            )

        print("STEP 6: File extension valid", flush=True)

        # Save Image
        filename = secure_filename(file.filename)

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        file.save(filepath)

        print(f"STEP 7: Image saved at {filepath}", flush=True)

        # Check file size
        print(f"STEP 8: Image size = {os.path.getsize(filepath)} bytes", flush=True)

        print("STEP 9: Calling predict_tumor()", flush=True)

        prediction, confidence, probabilities = predict_tumor(filepath)

        print("STEP 10: predict_tumor() completed", flush=True)

        print(f"Prediction = {prediction}", flush=True)
        print(f"Confidence = {confidence}", flush=True)

        print("=" * 60, flush=True)

        return render_template(
            "result.html",
            prediction=prediction,
            confidence=f"{confidence:.2f}%",
            probabilities=probabilities,
            image=filename
        )

    except Exception as e:

        print("=" * 60, flush=True)
        print("ERROR OCCURRED", flush=True)
        print(type(e).__name__, flush=True)
        print(str(e), flush=True)
        print("=" * 60, flush=True)

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
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )