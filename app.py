from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Merhaba, bu bir yapay zeka destekli PT uygulamasıdır!"

if __name__ == "__main__":
    app.run(debug=True)
