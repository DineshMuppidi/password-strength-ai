# password_project_notes 
---

Making a folder called venu
``` mkdir venv```

Activating that folder for virtual environment 
```source venv/bin/activate``` 

*Your prompt should now show (venv)—you’re in the virtual environment!
If you ever want to exit, just type deactivate (but stay in it for now).*

---

### Intall libraries
```pip install keras flask```  
*This will install keras and flask*

Create a python file in the project folder with conditions for a password. 
```
def check_password(password):
    # Basic rules for a strong password
    if len(password) < 8:
        return "Weak: Too short (minimum 8 characters)"
    elif not any(char.isupper() for char in password):
        return "Weak: Needs at least one uppercase letter"
    elif not any(char.isdigit() for char in password):
        return "Weak: Needs at least one number"
    elif not any(char in "!@#$%^&*" for char in password):
        return "Weak: Needs at least one special character (!@#$%^&*)"
    else:
        return "Strong: Looks good!"

# Get user input
user_password = input("Enter a password to check: ")
result = check_password(user_password)
print(result)
```
Run and check if its working    
```python <file_name.py>```

It’ll prompt you to “Enter a password to check:”

*Try a few:  
hello → "Weak: Too short..."
helloworld → "Weak: Needs uppercase..."
HelloWorld → "Weak: Needs number..."
HelloWorld1 → "Weak: Needs special..."
HelloWorld1! → "Strong: Looks good!"*


---
    

We want a function that:

* Generates a random password with letters (upper and lower), numbers, and special characters.
* Meets the “strong” criteria: at least 8 characters, one uppercase, one number, one special character.
* Lets the user specify the length (optional).

---

## Updated the code with Password generator

```
def generate_password(length=12):
    # Define character sets
    letters = string.ascii_letters  # a-z and A-Z
    digits = string.digits          # 0-9
    special_chars = "!@#$%^&*"
    
    # Ensure at least one of each required type
    password = [
        random.choice(string.ascii_uppercase),  # One uppercase
        random.choice(string.ascii_lowercase),  # One lowercase
        random.choice(digits),                  # One number
        random.choice(special_chars)            # One special
    ]
    
    # Fill the rest with random characters
    all_chars = letters + digits + special_chars
    for _ in range(length - 4):  # Subtract 4 because we added 4 already
        password.append(random.choice(all_chars))
    
    # Shuffle the password so it’s not predictable
    random.shuffle(password)
    
    # Join into a single string
    return "".join(password)

# Test the checker and generator
while True:
    choice = input("Type 'check' to test a password, 'generate' to create one, or 'quit' to exit: ").lower()
    if choice == "check":
        user_password = input("Enter a password to check: ")
        result = check_password(user_password)
        print(result)
    elif choice == "generate":
        length = int(input("Enter desired password length (minimum 8): "))
        if length < 8:
            print("Length must be at least 8 characters. Using 12 instead.")
            length = 12
        new_password = generate_password(length)
        print(f"Generated password: {new_password}")
        print(f"Strength: {check_password(new_password)}")
    elif choice == "quit":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
        
```
### What’s Happening?
New Imports: random (for picking random characters) and string (predefined sets like a-z, A-Z, 0-9).
generate_password(length=12):  

* Starts with one uppercase, lowercase, number, and special character to meet rules.  
* Fills the rest with random characters from all allowed sets.  
* Shuffles them so the required characters aren’t always first.
* Joins them into a string.  

Loop: A simple menu so you can keep checking or generating without restarting.

---

## Install more libraries

lets Install Extra Libraries   

```pip install tensorflow numpy pandas scikit-learn```


Update the code to train AI

```import random
import string
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

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

def preprocess_data(file_path="password_dataset.csv"):
    # Load dataset
    df = pd.read_csv(file_path)
    passwords = df["password"].values
    labels = df["label"].values

    # Convert passwords to numerical features (simple: length + char types)
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

    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def build_and_train_model(X_train, X_test, y_train, y_test):
    # Build a simple neural network
    model = Sequential([
        Dense(16, activation="relu", input_shape=(X_train.shape[1],)),
        Dense(8, activation="relu"),
        Dense(1, activation="sigmoid")  # 0 = weak, 1 = strong
    ])
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

    # Train the model
    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))
    return model

def predict_password_strength(model, password):
    # Convert password to features
    features = np.array([[
        len(password),
        int(any(c.isupper() for c in password)),
        int(any(c.isdigit() for c in password)),
        int(any(c in "!@#$%^&*" for c in password))
    ]])
    prediction = model.predict(features)[0][0]
    return "Strong" if prediction > 0.5 else "Weak"

if __name__ == "__main__":
    # Train the model
    X_train, X_test, y_train, y_test = preprocess_data()
    model = build_and_train_model(X_train, X_test, y_train, y_test)

    # Test it
    while True:
        choice = input("Type 'check' to test a password, 'generate' to create one, or 'quit' to exit: ").lower()
        if choice == "check":
            user_password = input("Enter a password to check: ")
            result = predict_password_strength(model, user_password)
            print(f"AI Prediction: {result}")
        elif choice == "generate":
            length = int(input("Enter desired password length (minimum 8): "))
            if length < 8:
                print("Length must be at least 8. Using 12 instead.")
                length = 12
            new_password = generate_password(length)
            result = predict_password_strength(model, new_password)
            print(f"Generated password: {new_password}")
            print(f"AI Prediction: {result}")
        elif choice == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

```
### What’s Happening?
* Dataset: We used our generated CSV (weak = 0, strong = 1).
* Preprocessing: Converted passwords to numbers (length, has uppercase, etc.)—a simple start (real projects use fancier text encoding, but this works for now).
* Model: A small neural network learns patterns from the data.
* Prediction: The AI guesses “Weak” or “Strong” based on what it learned.