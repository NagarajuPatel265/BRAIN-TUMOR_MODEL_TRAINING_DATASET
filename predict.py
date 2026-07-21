@app.route("/predict", methods=["POST"])
def predict():

    print("PREDICT ROUTE HIT", flush=True)

    return """
    <h1>Success!</h1>
    <h2>The /predict route is working.</h2>
    <a href="/">Go Back</a>
    """