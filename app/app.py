from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
     return "Flask App Deployed with CI/CD pipeline!"
     return "New version deployed!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

