import os
import random
import string
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from flask import Flask, request, render_template

app = Flask(__name__)

# Password generation function
def generate_password(length=12):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = "!@#$%^&*"
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    all_chars = letters + digits + special_chars
    for _ in range(length - 4):
        password.append(random.choice(all_chars))
    random.shuffle(password)
    return "".join(password)

# Data preprocessing
def preprocess_data(file_path="password_dataset.csv"):
    df = pd.read_csv(file_path)
    passwords = df["password"].values
    labels = df["label"].values
    features = []
    for pwd in passwords:
        feat = [
            len(pwd),
            int(any(c.isupper() for c in pwd)),
            int(any(c.isdigit() for c in pwd)),
            int(any(c in "!@#$%^&*" for c in pwd))
        ]
        features.append(feat)
    X = np.array(features)
    y = np.array(labels)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

# Train the model
def build_and_train_model(X_train, X_test, y_train, y_test):
    model = Sequential([
        Dense(16, activation="relu", input_shape=(X_train.shape[1],)),
        Dense(8, activation="relu"),
        Dense(1, activation="sigmoid")
    ])
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test), verbose=0)
    return model

# Predict strength
def predict_password_strength(model, password):
    features = np.array([[
        len(password),
        int(any(c.isupper() for c in password)),
        int(any(c.isdigit() for c in password)),
        int(any(c in "!@#$%^&*" for c in password))
    ]])
    prediction = model.predict(features, verbose=0)[0][0]
    return "Strong" if prediction > 0.5 else "Weak"

# Train model once at startup
X_train, X_test, y_train, y_test = preprocess_data()
model = build_and_train_model(X_train, X_test, y_train, y_test)

# Flask routes
@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    generated_password = None
    if request.method == "POST":
        if "check" in request.form:
            user_password = request.form["password"]
            result = predict_password_strength(model, user_password)
        elif "generate" in request.form:
            length = int(request.form.get("length", 12))
            if length < 8:
                length = 12
            generated_password = generate_password(length)
            result = predict_password_strength(model, generated_password)
    return render_template("index.html", result=result, generated_password=generated_password)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)