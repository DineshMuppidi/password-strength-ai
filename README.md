# AI-Powered Password Strength Checker

A web application that uses machine learning to evaluate password strength and generates secure passwords. Built as part of my Master’s in Cybersecurity with an AI emphasis.

## Features
- **Strength Checker**: Uses a neural network to classify passwords as "Weak" or "Strong."
- **Password Generator**: Creates random, secure passwords meeting complexity rules.
- **Web Interface**: Accessible via a Flask-powered site.

## Demo
Try it live: [https://dinesh-password-ai-5faa4d04becd.herokuapp.com/](https://dinesh-password-ai-5faa4d04becd.herokuapp.com/)

![Screenshot](https://private-user-images.githubusercontent.com/131384357/424678318-ce29499b-e5b2-417d-b58f-3c9845c09652.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDI0MTU3NjMsIm5iZiI6MTc0MjQxNTQ2MywicGF0aCI6Ii8xMzEzODQzNTcvNDI0Njc4MzE4LWNlMjk0OTliLWU1YjItNDE3ZC1iNThmLTNjOTg0NWMwOTY1Mi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzE5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMxOVQyMDE3NDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kMzM0ZjVjOTQyNWFlM2I2ZmQ5ZmU2MDcxZjhiY2Q3MGFlNjJhZGY2MzNkMDFmOTUzYWQ2Njg2YmMwOTNhZWRjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.lwkRTBOHlT46pubsjmtUErqlCKk_Kh0MEiCaKt4ZF24)

## Setup
1. Clone the repo: `git clone https://github.com/DineshMuppidi/password-strength-ai.git`
2. Navigate: `cd password-strength-ai`
3. Create virtual env: `python3 -m venv venv`
4. Activate: `source venv/bin/activate`
5. Install dependencies: `pip install tensorflow keras flask numpy pandas scikit-learn`
6. Run: `python password_checker.py`
7. Open `http://127.0.0.1:5000/` in a browser.

## Technologies
- **Python**: Core language.
- **Flask**: Web framework.
- **Keras/TensorFlow**: Neural network for AI classification.
- **Pandas/NumPy**: Data handling.
- **Scikit-learn**: Data preprocessing.

## Future Improvements
- Use a larger dataset (e.g., RockYou).
- Enhance AI with advanced features (e.g., n-gram analysis).

## Author
Dinesh Muppidi - Cybersecurity Master’s Student, USA  
[LinkedIn](https://linkedin.com/in/dineshmuppidi/) | [Email](mailto:muppididinesh@outlook.com)
