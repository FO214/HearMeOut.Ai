from flask import Flask, render_template, request
from test import program

app = Flask(__name__)
chat_history = []

@app.route("/", methods=["GET","POST"])
def home():
    if request.form.get("yessir") == "Yes":
        program(chat_history)
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug= True)